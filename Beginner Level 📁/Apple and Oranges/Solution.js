'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function countApplesAndOranges(start = s, end = t, appleTree = a, orangeTree = b, apples, oranges) {
    // Write your code here
    //calculate apple

    let countApple = 0;
    apples.map((distance) => {
        let eachDistance = appleTree + distance;
        if (eachDistance >= start && eachDistance <= end) {
            countApple++;
        }
        return countApple;
    })
    console.log(countApple)

    //calculate orange
    let countOrange = 0;
    oranges.map((distance) => {
        let eachDistance = orangeTree + distance;
        if (eachDistance >= start && eachDistance <= end) {
            countOrange++;
        }
        return countOrange;
    })

    console.log(countOrange)
}

function main() {
    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const s = parseInt(firstMultipleInput[0], 10);

    const t = parseInt(firstMultipleInput[1], 10);

    const secondMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const a = parseInt(secondMultipleInput[0], 10);

    const b = parseInt(secondMultipleInput[1], 10);

    const thirdMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const m = parseInt(thirdMultipleInput[0], 10);

    const n = parseInt(thirdMultipleInput[1], 10);

    const apples = readLine().replace(/\s+$/g, '').split(' ').map(applesTemp => parseInt(applesTemp, 10));

    const oranges = readLine().replace(/\s+$/g, '').split(' ').map(orangesTemp => parseInt(orangesTemp, 10));

    countApplesAndOranges(s, t, a, b, apples, oranges);
}