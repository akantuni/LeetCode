function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const newArr = []
    for (let i: number = 0; i < arr.length; i++) {
        newArr.push(fn(arr[i], i))
    }
    return newArr
};
