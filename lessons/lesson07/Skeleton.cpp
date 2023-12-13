#include "llvm/Pass.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;

namespace {

struct SkeletonPass : public PassInfoMixin<SkeletonPass> {
    PreservedAnalyses run(Module &M, ModuleAnalysisManager &AM) {
        for (auto &F : M) {
            // errs() << "I saw a function called " << F.getName() << "!\n";
			for (auto &B : F) {
				// errs() << "Basic block reached: " << B << "\n";
				for (auto &I : B) {
					errs() << "Instruction: " << I << "\n";  
					if (auto *op = dyn_cast<BinaryOperator>(&I)) {
						if (op->getOpcode() == Instruction::FDiv) {
							errs() << "You've found an FDIV!!!\n";
						}
					} 
				}
			}
        }
        return PreservedAnalyses::none();
    };
};

}

extern "C" LLVM_ATTRIBUTE_WEAK ::llvm::PassPluginLibraryInfo
llvmGetPassPluginInfo() {
    return {
        .APIVersion = LLVM_PLUGIN_API_VERSION,
        .PluginName = "Skeleton pass",
        .PluginVersion = "v0.1",
        .RegisterPassBuilderCallbacks = [](PassBuilder &PB) {
            PB.registerPipelineStartEPCallback(
                [](ModulePassManager &MPM, OptimizationLevel Level) {
                    MPM.addPass(SkeletonPass());
                });
        }
    };
}
