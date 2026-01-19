const DATA_URL = 'data/latest.json';
const numberFormat = new Intl.NumberFormat('en-CA', { maximumFractionDigits: 2 });
const intFormat = new Intl.NumberFormat('en-CA', { maximumFractionDigits: 0 });
const percentFormat = new Intl.NumberFormat('en-CA', { style: 'percent', maximumFractionDigits: 2 });

const badgeConfig = {
  near_gate: { label: 'Near Gate', tone: 'alert' },
  intrinsic_le_0: { label: 'Intrinsic <= 0', tone: 'alert' },
  nav_missing: { label: 'NAV Missing', tone: 'warn' },
  dist_suspended: { label: 'Dist Susp', tone: 'alert' },
  low_liquidity: { label: 'Low Liq', tone: 'warn' },
};

const tableConfigs = {
  classa: {
    label: 'Class A',
    defaultSort: { key: 'score_conservative', dir: -1 },
    rangeFilters: [
      { key: 'coverage', label: 'Coverage' },
      { key: 'discount_to_intrinsic', label: 'Discount to Intrinsic' },
      { key: 'years_to_maturity', label: 'Years to Maturity' },
    ],
    flagFilters: ['near_gate', 'intrinsic_le_0', 'nav_missing', 'low_liquidity', 'dist_suspended'],
    columns: [
      { key: 'ticker', label: 'Ticker', type: 'string', visible: true },
      { key: 'issuer_manager', label: 'Issuer', type: 'string', visible: true },
      { key: 'theme', label: 'Theme', type: 'string', visible: true },
      { key: 'price', label: 'Price', type: 'number', visible: true },
      { key: 'volume', label: 'Volume', type: 'integer', visible: true },
      { key: 'high_52w', label: '52W High', type: 'number', visible: true },
      { key: 'low_52w', label: '52W Low', type: 'number', visible: true },
      { key: 'unit_nav', label: 'Unit NAV', type: 'number', visible: true },
      { key: 'pref_par', label: 'Pref Par', type: 'number', visible: true },
      { key: 'coverage', label: 'Coverage', type: 'number', visible: true },
      { key: 'cushion', label: 'Cushion', type: 'number', visible: true },
      { key: 'gate_nav', label: 'Gate NAV', type: 'number', visible: true },
      { key: 'distance_to_gate', label: 'Distance to Gate', type: 'number', visible: true },
      { key: 'classa_intrinsic', label: 'Intrinsic', type: 'number', visible: true },
      { key: 'discount_to_intrinsic', label: 'Discount to Intrinsic', type: 'percent', visible: true },
      { key: 'annualized_discount_to_intrinsic', label: 'Annualized Discount', type: 'percent', visible: true },
      { key: 'years_to_maturity', label: 'Years to Maturity', type: 'number', visible: true },
      { key: 'dist_amt', label: 'Dist Amt', type: 'number', visible: true },
      { key: 'dist_freq', label: 'Dist Freq', type: 'string', visible: true },
      { key: 'dist_status', label: 'Dist Status', type: 'string', visible: true },
      { key: 'tr_1y', label: 'TR 1Y', type: 'percent', visible: true },
      { key: 'tr_3y', label: 'TR 3Y', type: 'percent', visible: true },
      { key: 'tr_5y', label: 'TR 5Y', type: 'percent', visible: true },
      { key: 'tr_10y', label: 'TR 10Y', type: 'percent', visible: true },
      { key: 'score_conservative', label: 'Score Cons', type: 'number', visible: true },
      { key: 'score_aggressive', label: 'Score Aggr', type: 'number', visible: true },
      { key: 'nav_self', label: 'NAV Self', type: 'number', visible: false },
      { key: 'discount_to_nav', label: 'Discount to NAV', type: 'percent', visible: false },
      { key: 'annualized_discount_to_nav', label: 'Annualized NAV Discount', type: 'percent', visible: false },
      { key: 'leverage_th', label: 'Leverage Th', type: 'number', visible: false },
      { key: 'leverage_mkt', label: 'Leverage Mkt', type: 'number', visible: false },
      { key: 'source_price', label: 'Source Price', type: 'string', visible: false },
      { key: 'source_nav', label: 'Source NAV', type: 'string', visible: false },
      { key: 'source_terms', label: 'Source Terms', type: 'string', visible: false },
    ],
  },
  preferred: {
    label: 'Preferred',
    defaultSort: { key: 'pref_yield_current', dir: -1 },
    rangeFilters: [
      { key: 'pref_yield_current', label: 'Current Yield' },
      { key: 'discount_to_par', label: 'Discount to Par' },
      { key: 'years_to_maturity', label: 'Years to Maturity' },
    ],
    flagFilters: ['near_gate', 'nav_missing', 'low_liquidity'],
    columns: [
      { key: 'ticker', label: 'Ticker', type: 'string', visible: true },
      { key: 'issuer_manager', label: 'Issuer', type: 'string', visible: true },
      { key: 'theme', label: 'Theme', type: 'string', visible: true },
      { key: 'price', label: 'Price', type: 'number', visible: true },
      { key: 'volume', label: 'Volume', type: 'integer', visible: true },
      { key: 'high_52w', label: '52W High', type: 'number', visible: true },
      { key: 'low_52w', label: '52W Low', type: 'number', visible: true },
      { key: 'pref_par', label: 'Pref Par', type: 'number', visible: true },
      { key: 'pref_div_amt', label: 'Pref Div Amt', type: 'number', visible: true },
      { key: 'pref_div_freq', label: 'Pref Div Freq', type: 'string', visible: true },
      { key: 'pref_yield_current', label: 'Current Yield', type: 'percent', visible: true },
      { key: 'discount_to_par', label: 'Discount to Par', type: 'percent', visible: true },
      { key: 'annualized_discount_to_par', label: 'Annualized Discount', type: 'percent', visible: true },
      { key: 'years_to_maturity', label: 'Years to Maturity', type: 'number', visible: true },
      { key: 'unit_nav', label: 'Unit NAV', type: 'number', visible: true },
      { key: 'coverage', label: 'Coverage', type: 'number', visible: true },
      { key: 'nav_self', label: 'NAV Self', type: 'number', visible: false },
      { key: 'discount_to_nav', label: 'Discount to NAV', type: 'percent', visible: false },
      { key: 'annualized_discount_to_nav', label: 'Annualized NAV Discount', type: 'percent', visible: false },
      { key: 'pref_yield_issue', label: 'Issue Yield', type: 'percent', visible: false },
      { key: 'gate_rule_text', label: 'Gate Rule', type: 'string', visible: false },
      { key: 'extendable', label: 'Extendable', type: 'boolean', visible: false },
      { key: 'source_price', label: 'Source Price', type: 'string', visible: false },
      { key: 'source_nav', label: 'Source NAV', type: 'string', visible: false },
      { key: 'source_terms', label: 'Source Terms', type: 'string', visible: false },
    ],
  },
};

function formatValue(value, type) {
  if (value === null || value === undefined || value === '') return '--';
  if (type === 'percent') return percentFormat.format(value);
  if (type === 'integer') return intFormat.format(value);
  if (type === 'number') return numberFormat.format(value);
  if (type === 'boolean') return value ? 'Yes' : 'No';
  return String(value);
}

function toComparable(value, type) {
  if (value === null || value === undefined) return null;
  if (type === 'percent' || type === 'number' || type === 'integer') return Number(value);
  if (type === 'boolean') return value ? 1 : 0;
  return String(value).toLowerCase();
}

function csvEscape(value) {
function formatAsOf(value) {
  if (!value) return '--';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  const parts = new Intl.DateTimeFormat('en-CA', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    timeZoneName: 'short',
  }).formatToParts(date);
  const map = Object.fromEntries(parts.map((part) => [part.type, part.value]));
  const tz = map.timeZoneName ? ` ${map.timeZoneName}` : '';
  return `${map.year}-${map.month}-${map.day} ${map.hour}:${map.minute}${tz}`;
}

  if (value === null || value === undefined) return '';
  const text = String(value);
  if (text.includes(',') || text.includes('"') || text.includes('\n')) {
    return '"' + text.replace(/"/g, '""') + '"';
  }
  return text;
}

function buildBadgeHtml(row) {
  const badges = [];
  Object.keys(badgeConfig).forEach((key) => {
    if (row[key]) {
      const config = badgeConfig[key];
      badges.push(`<span class="badge ${config.tone}" title="${config.label}">${config.label}</span>`);
    }
  });
  if (!badges.length) return '';
  return `<span class="badges">${badges.join('')}</span>`;
}

function applyFilters(rows, state, config) {
  return rows.filter((row) => {
    if (state.search) {
      const haystack = `${row.ticker || ''} ${row.issuer_manager || ''} ${row.theme || ''}`.toLowerCase();
      if (!haystack.includes(state.search)) return false;
    }

    for (const filter of config.rangeFilters) {
      const value = row[filter.key];
      const { min, max } = state.ranges[filter.key] || {};
      if (min !== '' && value !== null && value !== undefined && Number(value) < Number(min)) return false;
      if (max !== '' && value !== null && value !== undefined && Number(value) > Number(max)) return false;
    }

    for (const key of config.flagFilters) {
      if (state.flags[key] && !row[key]) return false;
    }

    return true;
  });
}

function sortRows(rows, state, config) {
  if (!state.sortKey) return rows;
  const col = config.columns.find((item) => item.key === state.sortKey);
  const type = col ? col.type : 'string';
  const dir = state.sortDir;

  return [...rows].sort((a, b) => {
    const aVal = toComparable(a[state.sortKey], type);
    const bVal = toComparable(b[state.sortKey], type);
    if (aVal === null && bVal === null) return 0;
    if (aVal === null) return 1;
    if (bVal === null) return -1;
    if (aVal < bVal) return -1 * dir;
    if (aVal > bVal) return 1 * dir;
    return 0;
  });
}

function renderTable(section, rows, state, config) {
  const table = section.querySelector('table');
  const thead = table.querySelector('thead');
  const tbody = table.querySelector('tbody');

  const visibleColumns = config.columns.filter((col) => state.visibleColumns.has(col.key));

  thead.innerHTML = '';
  const headerRow = document.createElement('tr');
  visibleColumns.forEach((col) => {
    const th = document.createElement('th');
    th.textContent = col.label;
    if (state.sortKey === col.key) {
      th.textContent += state.sortDir === 1 ? ' ^' : ' v';
    }
    th.addEventListener('click', () => {
      if (state.sortKey === col.key) {
        state.sortDir = state.sortDir * -1;
      } else {
        state.sortKey = col.key;
        state.sortDir = -1;
      }
      renderTable(section, rows, state, config);
    });
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);

  tbody.innerHTML = '';
  const filtered = applyFilters(rows, state, config);
  const sorted = sortRows(filtered, state, config);

  sorted.forEach((row) => {
    const tr = document.createElement('tr');
    visibleColumns.forEach((col) => {
      const td = document.createElement('td');
      if (col.key === 'ticker') {
        td.innerHTML = `${formatValue(row[col.key], col.type)}${buildBadgeHtml(row)}`;
      } else {
        td.textContent = formatValue(row[col.key], col.type);
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  section.dataset.filteredCount = String(sorted.length);
}

function initControls(section, rows, config) {
  const state = {
    search: '',
    sortKey: config.defaultSort.key,
    sortDir: config.defaultSort.dir,
    ranges: {},
    flags: {},
    visibleColumns: new Set(),
  };

  config.columns.forEach((col) => {
    if (col.visible) state.visibleColumns.add(col.key);
  });

  const searchInput = section.querySelector('[data-search]');
  searchInput.addEventListener('input', (event) => {
    state.search = event.target.value.toLowerCase();
    renderTable(section, rows, state, config);
  });

  const rangeContainer = section.querySelector('[data-range-filters]');
  rangeContainer.innerHTML = '<label>Range filters</label>';
  config.rangeFilters.forEach((filter) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'range-group';

    const minInput = document.createElement('input');
    minInput.type = 'number';
    minInput.placeholder = `${filter.label} min`;
    minInput.step = 'any';

    const maxInput = document.createElement('input');
    maxInput.type = 'number';
    maxInput.placeholder = `${filter.label} max`;
    maxInput.step = 'any';

    state.ranges[filter.key] = { min: '', max: '' };

    minInput.addEventListener('input', () => {
      state.ranges[filter.key].min = minInput.value;
      renderTable(section, rows, state, config);
    });
    maxInput.addEventListener('input', () => {
      state.ranges[filter.key].max = maxInput.value;
      renderTable(section, rows, state, config);
    });

    wrapper.appendChild(minInput);
    wrapper.appendChild(maxInput);
    rangeContainer.appendChild(wrapper);
  });

  const flagContainer = section.querySelector('[data-flag-filters]');
  const flagLabel = document.createElement('label');
  flagLabel.textContent = 'Risk filters';
  flagContainer.appendChild(flagLabel);
  const flagGroup = document.createElement('div');
  flagGroup.className = 'flag-group';
  config.flagFilters.forEach((flagKey) => {
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.addEventListener('change', () => {
      state.flags[flagKey] = input.checked;
      renderTable(section, rows, state, config);
    });
    label.appendChild(input);
    label.appendChild(document.createTextNode(badgeConfig[flagKey].label));
    flagGroup.appendChild(label);
  });
  flagContainer.appendChild(flagGroup);

  const columnContainer = section.querySelector('[data-column-toggles]');
  const columnLabel = document.createElement('label');
  columnLabel.textContent = 'Columns';
  columnContainer.appendChild(columnLabel);
  const columnGroup = document.createElement('div');
  columnGroup.className = 'column-group';
  config.columns.forEach((col) => {
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.checked = state.visibleColumns.has(col.key);
    input.addEventListener('change', () => {
      if (input.checked) state.visibleColumns.add(col.key);
      else state.visibleColumns.delete(col.key);
      renderTable(section, rows, state, config);
    });
    label.appendChild(input);
    label.appendChild(document.createTextNode(col.label));
    columnGroup.appendChild(label);
  });
  columnContainer.appendChild(columnGroup);

  section.querySelector('[data-export]').addEventListener('click', () => {
    const filtered = applyFilters(rows, state, config);
    const sorted = sortRows(filtered, state, config);
    const visibleColumns = config.columns.filter((col) => state.visibleColumns.has(col.key));
    const header = visibleColumns.map((col) => csvEscape(col.label)).join(',');
    const body = sorted.map((row) => {
      return visibleColumns.map((col) => csvEscape(row[col.key])).join(',');
    });
    const csv = [header, ...body].join('\n');
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${config.label.toLowerCase()}-filtered.csv`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  });

  section.querySelector('[data-reset]').addEventListener('click', () => {
    state.search = '';
    searchInput.value = '';
    config.rangeFilters.forEach((filter) => {
      state.ranges[filter.key] = { min: '', max: '' };
    });
    section.querySelectorAll('[data-range-filters] input').forEach((input) => {
      input.value = '';
    });
    section.querySelectorAll('[data-flag-filters] input[type="checkbox"]').forEach((input) => {
      input.checked = false;
    });
    Object.keys(state.flags).forEach((key) => {
      state.flags[key] = false;
    });
    state.visibleColumns = new Set();
    config.columns.forEach((col) => {
      if (col.visible) state.visibleColumns.add(col.key);
    });
    section.querySelectorAll('[data-column-toggles] input[type="checkbox"]').forEach((input, index) => {
      input.checked = config.columns[index].visible;
    });
    state.sortKey = config.defaultSort.key;
    state.sortDir = config.defaultSort.dir;
    renderTable(section, rows, state, config);
  });

  renderTable(section, rows, state, config);
}

function initTabs() {
  const buttons = document.querySelectorAll('.tab-button');
  const panels = document.querySelectorAll('.tab-panel');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      buttons.forEach((btn) => btn.classList.remove('active'));
      panels.forEach((panel) => panel.classList.remove('active'));
      button.classList.add('active');
      document.getElementById(`tab-${button.dataset.tab}`).classList.add('active');
    });
  });
}

function updateMeta(rows) {
  const asof = rows[0]?.asof;
  document.getElementById('asof').textContent = formatAsOf(asof);
  document.getElementById('row-count').textContent = rows.length;
}

async function init() {
  const response = await fetch(DATA_URL);
  const data = await response.json();

  if (!Array.isArray(data)) return;

  updateMeta(data);

  const classARows = data.filter((row) => row.security_type === 'CLASS_A');
  const preferredRows = data.filter((row) => row.security_type === 'PREFERRED');

  const classSection = document.querySelector('[data-table="classa"]');
  const prefSection = document.querySelector('[data-table="preferred"]');

  initControls(classSection, classARows, tableConfigs.classa);
  initControls(prefSection, preferredRows, tableConfigs.preferred);
  initTabs();
}

init();
