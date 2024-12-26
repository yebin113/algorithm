function solution(s){
    if (s[0] === ")" || s[s.length-1]==="("){
        return false
    }
    let open = 0
    for (let i=0;i<s.length;i++){
        if (s[i] === "("){
            open += 1
        } else {
            open -= 1
        }
        if (open < 0) {
            return false
        }
    }
    if (open !== 0) {
        return false
    }
    else return true;
}