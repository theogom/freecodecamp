const telephoneCheck = require('./telephoneChecker').telephoneCheck;

test('Valid telephone number', () => {
    expect(telephoneCheck('555 555 5555'))
    .toBe(true);

    expect(telephoneCheck('555-555-5555'))
    .toBe(true);

    expect(telephoneCheck('(555)555-5555'))
    .toBe(true);

    expect(telephoneCheck('(555) 555-5555'))
    .toBe(true);

    expect(telephoneCheck('5555555555'))
    .toBe(true);

    expect(telephoneCheck('1 555 555 5555'))
    .toBe(true);

    expect(telephoneCheck('1 555-555-5555'))
    .toBe(true);

    expect(telephoneCheck('1(555)555-5555'))
    .toBe(true);

    expect(telephoneCheck('1 456 789 4444'))
    .toBe(true);
});

test('Invalid telephone number', () => {
    expect(telephoneCheck('555-5555'))
    .toBe(false);

    expect(telephoneCheck('5555555'))
    .toBe(false);

    expect(telephoneCheck('1 555)555-5555'))
    .toBe(false);

    expect(telephoneCheck('123**&!!asdf#'))
    .toBe(false);

    expect(telephoneCheck('(6054756961)'))
    .toBe(false);

    expect(telephoneCheck('55555555'))
    .toBe(false);

    expect(telephoneCheck('2 (757) 622-7382'))
    .toBe(false);
});