import os
from shutil import copyfile
from shutil import rmtree

GIT_CLONE_COMMAND = 'git clone '

PROTOCOL_SPEC_MASTER = 'https://github.com/smartdevicelink/protocol_spec.git'
PROTOCOL_SPEC_GIT_DIR = 'protocolSpecTemp'
PROTOCOL_SPEC_DOC_LOCATION = '../docs/Protocol Spec/index.md'

RPC_SPEC_MASTER = 'https://github.com/smartdevicelink/rpc_spec.git'
RPC_SPEC_GIT_DIR = 'rpcSpecTemp'
RPC_SPEC_DOC_LOCATION = '../docs/RPC Spec/index.md'

print('Starting process')

os.system(GIT_CLONE_COMMAND + PROTOCOL_SPEC_MASTER + ' ' + PROTOCOL_SPEC_GIT_DIR)
copyfile(PROTOCOL_SPEC_GIT_DIR + "/README.md", PROTOCOL_SPEC_DOC_LOCATION)
rmtree(PROTOCOL_SPEC_GIT_DIR)

print('Completed Protocol Spec retrieval. Starting RPC Spec.')


os.system(GIT_CLONE_COMMAND + RPC_SPEC_MASTER + ' ' + RPC_SPEC_GIT_DIR)
copyfile(RPC_SPEC_GIT_DIR+"/README.md", RPC_SPEC_DOC_LOCATION)
rmtree(RPC_SPEC_GIT_DIR)


print('Completed RPC Spec retrieval. Finished.')
