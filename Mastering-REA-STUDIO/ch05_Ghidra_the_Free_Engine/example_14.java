import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

public class ListFunctions extends GhidraScript {
    @Override
    protected void run() throws Exception {
        var fm = currentProgram.getFunctionManager();
        for (Function f : fm.getFunctions(true)) {
            long size = f.getBody().getNumAddresses();
            println(f.getEntryPoint() + " "
                + f.getName() + " " + size);
        }
    }
}
