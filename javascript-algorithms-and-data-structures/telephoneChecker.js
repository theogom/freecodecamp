function telephoneCheck(tel) {
    return /^(1\s?)?(\d{3}|\(\d{3}\))[\s\-]?\d{3}[\s\-]?\d{4}$/.test(tel);
}

telephoneCheck("1 555 555 5555");

exports.telephoneCheck = telephoneCheck;
