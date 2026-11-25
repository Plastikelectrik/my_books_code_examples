const libc = Process.getModuleByName("libc.so.6");
const strcmp = libc.getExportByName("strcmp");
Interceptor.attach(strcmp, {
  onEnter(args) {
    this.a = args[0].readUtf8String();
    this.b = args[1].readUtf8String();
  },
  onLeave(ret) {
    const r = ret.toInt32();
    console.log(`strcmp(${this.a}, ${this.b}) = ${r}`);
  },
});
