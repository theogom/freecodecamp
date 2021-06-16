const currencies = {
    'ONE HUNDRED': 100,
    'TWENTY': 20,
    'TEN': 10,
    'FIVE': 5,
    'ONE': 1,
    'QUARTER': 0.25,
    'DIME': 0.1,
    'NICKEL': 0.05,
    'PENNY': 0.01
};

function checkCashRegister(price, cash, cid) {
    let changeAmount = cash - price;
    const changeValues = [];
    let all = true;
    console.log(cid);

    cid
        .slice(0) // To copy the array in order not to reverse the original
        .reverse()
        .forEach(currency => {
            const [id, amount] = currency;
            const value = currencies[id];
            const inRegister = Math.round(amount / value);
            const inChange = Math.floor(changeAmount / value);
            const number = Math.min(inChange, inRegister);
            changeAmount = Number(Math.round((changeAmount - number * value) + 'e2') + 'e-2'); // Prevent rounding errors by using exp notations https://www.jacklmoore.com/notes/rounding-in-javascript/
            all = number == inRegister ? all : false;
            if (number > 0)
                changeValues.push([id, number * value]);
        });
    const status = changeAmount > 0 ? 'INSUFFICIENT_FUNDS' :
        all ? 'CLOSED' :
            'OPEN';

    const change = status === 'INSUFFICIENT_FUNDS' ? [] :
        status === 'CLOSED' ? cid :
            changeValues;
    console.log(cid);

    return { status, change };
}
