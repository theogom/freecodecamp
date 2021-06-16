const shiftChar = require('./caesar').shiftChar;
const rot13 = require('./caesar').rot13;

describe('Shift char', () => {
    test('Shift char to the right', () => {
        expect(shiftChar('A', 1))
        .toBe('B');

        expect(shiftChar('E', 5))
        .toBe('J');
    });

    test('Shift char to the right with overflow', () => {
        expect(shiftChar('Z', 1))
        .toBe('A');

        expect(shiftChar('Y', 5))
        .toBe('D');
    });
});

describe('ROT13 cipher', () => {
    test('One word', () => {
        expect(rot13('SERRPBQRPNZC'))
            .toBe('FREECODECAMP');
    });

    test('Sentence', () => {
        expect(rot13('SERR PBQR PNZC'))
            .toBe('FREE CODE CAMP');

        expect(rot13('GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT'))
            .toBe('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG');
    });

    test('Sentence with punctuation', () => {
        expect(rot13('SERR CVMMN!'))
            .toBe('FREE PIZZA!');

        expect(rot13('SERR YBIR?'))
            .toBe('FREE LOVE?');

        expect(rot13('GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.'))
            .toBe('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.');
    });
});
