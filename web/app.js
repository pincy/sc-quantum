const TEXT = new Set([0, 2, 3, 22]);
const DEFAULT_SORT = [{ column: 'c5', dir: 'desc' }];
const FLIGHT = [14, 15, 16, 17, 18, 19];
const GROUPS = [
  ['Ship', 'g-combo', [0]],
  ['Setup', 'g-combo', [1, 2, 3]],
  ['Range', 'g-range', [4, 5]],
  ['Drive', 'g-drive', [6, 7, 8]],
  ['Ship stats', 'g-ship', [9, 10]],
  ['Price (aUEC)', 'g-price', [11, 12, 13]],
  ['Flight time', 'g-flight', [14, 15, 16, 17, 18, 19]],
  ['Details', 'g-misc', [20, 21, 22]],
];

const $ = id => document.getElementById(id);
const fmt = v => typeof v === 'number' ? v.toLocaleString('en-US') : v;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

document.title = `SC ${VERSION} Quantum Ranking`;
$('version').textContent = VERSION;

// Theme
const setThemeLabel = () => { $('theme').textContent = document.documentElement.dataset.theme === 'dark' ? '☀ Light' : '☾ Dark'; };
$('theme').addEventListener('click', () => {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  localStorage.setItem('theme', next);
  setThemeLabel();
});
setThemeLabel();

// Value statistics for bars and color scale
const stats = {};
HEAD.forEach((_, i) => {
  const vals = ROWS.map(r => r[i]).filter(v => typeof v === 'number');
  stats[i] = { min: Math.min(...vals), max: Math.max(...vals) };
});

const hidden = new Set(JSON.parse(localStorage.getItem('hiddenCols') || '[]'));

function formatter(i) {
  if (i === 3) return cell => {
    const v = cell.getValue() || '';
    const [g, cls] = v.split(' - ');
    return `<span class="chip grade-${esc(g)}">${esc(g)}</span>${cls ? `<span class="cls">${esc(cls)}</span>` : ''}`;
  };
  if (i === 5) return cell => {
    const v = cell.getValue();
    return v === null ? '' : `<div class="bar" style="--w:${(v / stats[5].max * 100).toFixed(1)}%"><span>${fmt(v)}</span></div>`;
  };
  if (FLIGHT.includes(i)) return cell => {
    const v = cell.getValue();
    if (v === null) return '';
    const { min, max } = stats[i];
    const t = max > min ? (v - min) / (max - min) : 0;
    return `<span class="heat" style="background:hsla(${Math.round(140 * (1 - t))},70%,50%,.22)">${fmt(v)}</span>`;
  };
  if (i === 22) return cell => cell.getValue() ? '<span class="stock-mark">✓</span>' : '';
  return cell => { const v = cell.getValue(); return v === null ? '' : fmt(v); };
}

const columns = GROUPS.map(([title, cssClass, idx]) => ({
  title,
  cssClass,
  frozen: idx[0] === 0,
  columns: idx.map(i => ({
    title: HEAD[i],
    field: 'c' + i,
    visible: !hidden.has('c' + i),
    sorter: TEXT.has(i) ? 'string' : 'number',
    sorterParams: { alwaysEmptyLast: true },
    headerSortStartingDir: TEXT.has(i) ? 'asc' : 'desc',
    hozAlign: i === 22 ? 'center' : TEXT.has(i) ? 'left' : 'right',
    formatter: formatter(i),
  })),
}));

const data = ROWS.map(r => Object.fromEntries(r.map((v, i) => ['c' + i, v])));

const table = new Tabulator('#table', {
  data,
  columns,
  height: '72vh',
  layout: 'fitDataFill',
  columnHeaderSortMulti: true,
  initialSort: DEFAULT_SORT,
});

// Filters
let size = '';
const grades = new Set();

function applyFilters() {
  const q = $('q').value.trim().toLowerCase(), c = +$('cargo').value || 0;
  const maxPrice = $('price').value === '' ? null : +$('price').value * 1e6;
  const st = $('stock').checked, pr = $('priced').checked;
  table.setFilter(d => {
    if (size && d.c1 != size) return false;
    if (grades.size && !grades.has((d.c3 || '').charAt(0))) return false;
    if (d.c9 < c) return false;
    if (st && !d.c22) return false;
    if (pr && d.c13 === null) return false;
    if (maxPrice !== null) {
      const price = d.c13 !== null ? d.c13 : (d.c22 ? d.c11 : null);
      if (price === null || price > maxPrice) return false;
    }
    return !q || (d.c0 + ' ' + d.c2).toLowerCase().includes(q);
  });
}

let timer;
const debounced = () => { clearTimeout(timer); timer = setTimeout(applyFilters, 150); };
$('q').addEventListener('input', debounced);
$('price').addEventListener('input', debounced);
['cargo', 'stock', 'priced'].forEach(id => $(id).addEventListener('input', applyFilters));

$('size').addEventListener('click', e => {
  if (e.target.tagName !== 'BUTTON') return;
  size = e.target.dataset.v;
  $('size').querySelectorAll('button').forEach(b => b.classList.toggle('on', b === e.target));
  applyFilters();
});
$('grade').addEventListener('click', e => {
  if (e.target.tagName !== 'BUTTON') return;
  const g = e.target.dataset.v;
  grades.has(g) ? grades.delete(g) : grades.add(g);
  e.target.classList.toggle('on', grades.has(g));
  applyFilters();
});
$('reset').addEventListener('click', () => table.setSort(DEFAULT_SORT));

// Column menu
$('colpop').innerHTML = HEAD.map((h, i) => i === 0 ? '' :
  `<label><input type="checkbox" data-f="c${i}" ${hidden.has('c' + i) ? '' : 'checked'}>${esc(h)}</label>`).join('');
$('colpop').addEventListener('change', e => {
  const f = e.target.dataset.f;
  if (e.target.checked) { hidden.delete(f); table.showColumn(f); } else { hidden.add(f); table.hideColumn(f); }
  localStorage.setItem('hiddenCols', JSON.stringify([...hidden]));
});
$('colbtn').addEventListener('click', e => { e.stopPropagation(); $('colmenu').classList.toggle('open'); });
document.addEventListener('click', e => { if (!$('colmenu').contains(e.target)) $('colmenu').classList.remove('open'); });

const setCount = n => { $('count').textContent = `${n} of ${ROWS.length}`; };
table.on('tableBuilt', () => setCount(ROWS.length));
table.on('dataFiltered', (filters, rows) => setCount(rows.length));
