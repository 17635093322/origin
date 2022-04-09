module.paths.push("C:\\Users\\zq125\\AppData\\Roaming\\npm\\node_modules")
var oo = require('crypto-js')
function h(t) {
    var e = oo.enc.Hex.parse(t)
      , n = oo.enc.Base64.stringify(e)
      , f = oo.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
      , m = oo.enc.Utf8.parse("0123456789ABCDEF")
      , a = oo.AES.decrypt(n, f, {
        iv: m,
        mode: oo.mode.CBC,
        padding: oo.pad.Pkcs7
    })
      , r = a.toString(oo.enc.Utf8);
    return r.toString()
}
