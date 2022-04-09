var n = require("crypto-js")
function i() {
    for (var t = Math.round((new Date).getTime() / 1e3).toString(), e = arguments.length, r = new Array(e), i = 0; i < e; i++)
        r[i] = arguments[i];
    // console.log(r)
    r.push(t);
    var o = n.SHA1(r.join(",")).toString(n.enc.Hex);
    var c = n.enc.Base64.stringify(n.enc.Utf8.parse([o, t].join(",")));
    return c
}
function params(page_num) {
    var a = page_num * 10;
    var e = i('/api/movie', a);
    return e
}