/*
Caesar ROT13 cipher for uppercase-only strings
*/

function shiftChar(char, number) {
    return String.fromCharCode((char.charCodeAt(0) - 'A'.charCodeAt(0) + number) % 26 + 'A'.charCodeAt(0));
}

function rot13(str) {
    return str.replace(/[A-Z]/g, (char) => shiftChar(char, 13));
}

exports.shiftChar = shiftChar;
exports.rot13 = rot13;
