const romanNumerals = {
    1: 'I',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1000: 'M'
}

const romanSpecials = {
    'IIII': 'IV',
    'VIIII': 'IX',
    'VIV': 'IX',
    'XXXX': 'XL',
    'LXXXX': 'XC',
    'LXL': 'XC',
    'CCCC': 'CD',
    'DCCCC': 'CM',
    'DCD': 'CM'
}

function convertToRoman(num) {
    if (typeof (num) !== 'number')
        throw 'Input should be a number';

    if (num < 0)
        throw 'Can not convert negative number';

    let roman = '';

    Object.keys(romanNumerals)
        .reverse()
        .forEach(decimal => {
            roman += romanNumerals[decimal].repeat(Math.floor(num / decimal));
            num %= decimal;
        });

    Object.keys(romanSpecials)
        .forEach(special => {
            roman = roman.replace(special, romanSpecials[special]);
        });

    return roman;
}

exports.convertToRoman = convertToRoman;