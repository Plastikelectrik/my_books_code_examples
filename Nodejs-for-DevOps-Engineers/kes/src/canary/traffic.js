// Traffic routers: anything with setCanary(weight) (Chapter 13).
export function loggingRouter(inner, log) {
  return {
    async setCanary(weight) {
      log(`traffic: canary ${weight}%`);
      await inner.setCanary(weight);
    },
  };
}

export function memoryRouter() {
  const history = [];
  return {
    history,
    async setCanary(w) { history.push(w); },
  };
}
