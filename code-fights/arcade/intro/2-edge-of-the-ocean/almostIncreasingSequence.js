function isGreaterEqualThanNext(index, sequence) {
    return sequence[index] >= sequence[index+1];
}

function isNextGreaterThanPrev(index, sequence) {
    return sequence[index+1] > sequence[index-1];
}

function isGreaterEqualThanPrevious(index, sequence) {
    return sequence[index] > sequence[index-1];
}

function isSmallerThanNextAndPrevious(index, sequence) {
    return sequence[index] < sequence[index+1] && sequence[index] < sequence[index-1];
}

function hasPrevious(index, sequence) {
    return sequence[index-1] != undefined;
}

function hasNext(index, sequence) {
    return sequence[index+1] != undefined;
}

function checkSequence(sequence) {
    for (let i = 0; i < sequence.length; i++)
        if(isGreaterEqualThanNext(i, sequence)) return false;
    return true;
}

function almostIncreasingSequence(sequence) {
    let count = 0;
    for (let i = 0; i < sequence.length; i++) {
        if (count == 0) {
            if (!hasPrevious(i,sequence) && isGreaterEqualThanNext(i,sequence)) {
                sequence.splice(i, 1);
                count++;
            } else if (isGreaterEqualThanNext(i,sequence) && isNextGreaterThanPrev(i, sequence)) {
                sequence.splice(i, 1);
                count++;
            } else if (!hasNext(i,sequence) && !isGreaterEqualThanPrevious(i, sequence)) {
                sequence.splice(i, 1);
                count++;
            } else if (isSmallerThanNextAndPrevious(i, sequence)) {
                sequence.splice(i, 1);
                count++;
            }
        }
    }

    return checkSequence(sequence);
}
