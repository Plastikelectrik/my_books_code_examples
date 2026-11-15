// Book: Node.js for DevOps Engineers — Example 107
// test/helpers/http-mock.js
import {
  MockAgent, setGlobalDispatcher, getGlobalDispatcher,
} from 'undici';

export function httpMock(t, origin) {
  const previous = getGlobalDispatcher();
  const agent = new MockAgent();
  agent.disableNetConnect();
  setGlobalDispatcher(agent);
  t.after(() => {
    agent.assertNoPendingInterceptors();
    setGlobalDispatcher(previous);
  });
  return agent.get(origin);
}
