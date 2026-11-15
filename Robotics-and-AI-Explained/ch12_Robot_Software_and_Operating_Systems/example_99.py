# Sequence and fallback nodes for a pick-up task
SUCCESS, FAILURE = "SUCCESS", "FAILURE"

def sequence(*children):
    def run(bb):
        for child in children:
            if child(bb) == FAILURE:
                return FAILURE
        return SUCCESS
    return run

def fallback(*children):
    def run(bb):
        for child in children:
            if child(bb) == SUCCESS:
                return SUCCESS
        return FAILURE
    return run

def check(key):
    return lambda bb: SUCCESS if bb.get(key) else FAILURE

def act(name, result=SUCCESS):
    def run(bb):
        print("  action:", name)
        return result
    return run

tree = sequence(
    fallback(check("battery_ok"), act("go charge")),
    fallback(check("object_visible"), act("search")),
    act("grasp object"),
    act("bring to table"))

cases = [{"battery_ok": True, "object_visible": True},
         {"battery_ok": False, "object_visible": False}]
for bb in cases:
    print("blackboard:", bb)
    print("result:", tree(bb))
