//  동전 0,1 번갈아 나오게 뒤집기

function solution(A) {
    min = A.length;
    for (var k = 0; k <= 1; k++) {
        var cnt = 0;
        var next = k;
        for (var i = 0; i < A.length; i++) {
            if (next != A[i]) {
                cnt++;
            }
            next = (next == 1 ? 0 : 1);
        }
        min = Math.min(cnt, min);
    }
    console.log(min)
    return
}
solution([0, 1, 1, 0])