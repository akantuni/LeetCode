type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        let ans = x
        for (let f of functions.reverse()) {
            ans = f(ans)
        }
        return ans
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
