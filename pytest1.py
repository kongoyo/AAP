from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# 初始化 DataLoader（用於加載 playbook 和變數）
loader = DataLoader()

# 設定 inventory（可以是文件或動態生成）
inventory = InventoryManager(loader=loader, sources='localhost,')

# 設定變數管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 設定 context（Ansible 的全局設定）
context.CLIARGS = ImmutableDict(
    connection='local',  # 使用本地連接
    module_path=['/path/to/modules'],  # 自定義模組路徑
    forks=10,  # 並行執行任務的數量
    become=None,  # 是否切換用戶
    become_method=None,  # 切換用戶的方法（如 sudo）
    become_user=None,  # 切換到的用戶
    check=False,  # 是否只檢查而不執行
    diff=False,  # 是否顯示差異
)

# 設定 playbook 路徑
playbook_path = '/root/AAP/ibmi_test1.yml'

# 初始化 PlaybookExecutor
executor = PlaybookExecutor(
    playbooks=[playbook_path],
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords={},  # 如果需要密碼，可以在這裡提供
)

# 執行 playbook
results = executor.run()

# 輸出結果
print(results)