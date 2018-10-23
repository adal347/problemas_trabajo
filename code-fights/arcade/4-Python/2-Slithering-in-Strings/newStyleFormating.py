def newStyleFormatting(s):
    return re.sub('pct_var', '%', re.sub('%[bcdefgnosx]', '{}', re.sub('%%', 'pct_var', s)))
