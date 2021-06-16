const convertToRoman = require('./roman').convertToRoman;

test('Simple number', () => {
    expect(convertToRoman(1))
    .toBe('I');

    expect(convertToRoman(6))
    .toBe('VI');

    expect(convertToRoman(16))
    .toBe('XVI');

    expect(convertToRoman(66))
    .toBe('LXVI');

    expect(convertToRoman(166))
    .toBe('CLXVI');

    expect(convertToRoman(666))
    .toBe('DCLXVI');

    expect(convertToRoman(1666))
    .toBe('MDCLXVI');
});

test('Number with multiple same symbol', () =>  {
    expect(convertToRoman(3))
    .toBe('III');

    expect(convertToRoman(8))
    .toBe('VIII');

    expect(convertToRoman(30))
    .toBe('XXX');

    expect(convertToRoman(23))
    .toBe('XXIII');

    expect(convertToRoman(200))
    .toBe('CC');

    expect(convertToRoman(232))
    .toBe('CCXXXII');

    expect(convertToRoman(2000))
    .toBe('MM');

    expect(convertToRoman(2320))
    .toBe('MMCCCXX');

})

test('Special number', () => {
    expect(convertToRoman(4))
    .toBe('IV');

    expect(convertToRoman(14))
    .toBe('XIV');

    expect(convertToRoman(9))
    .toBe('IX');

    expect(convertToRoman(59))
    .toBe('LIX');

    expect(convertToRoman(40))
    .toBe('XL');

    expect(convertToRoman(42))
    .toBe('XLII');

    expect(convertToRoman(90))
    .toBe('XC');

    expect(convertToRoman(99))
    .toBe('XCIX');

    expect(convertToRoman(400))
    .toBe('CD');

    expect(convertToRoman(460))
    .toBe('CDLX');

    expect(convertToRoman(900))
    .toBe('CM');

    expect(convertToRoman(916))
    .toBe('CMXVI');
});