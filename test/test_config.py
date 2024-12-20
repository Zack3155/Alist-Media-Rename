import filecmp
import os
from unittest import mock
from AlistMediaRename import Config


@mock.patch("builtins.input")
def test_config_file_is_not_exist(mocked_input):
    """
    测试环境:
    1. 初次运行，配置文件不存在
    2. 默认配置文件存在，但未更新
    预期结果: 程序自动创建配置文件
    测试步骤:
    1. 模拟用户输入为空
    2. 捕获并忽略 SystemExit 异常
    3. 比较生成的配置文件与默认文件
    4. 删除生成的配置文件
    """
    # 模拟用户输入
    mocked_input.side_effect = [" ", "", "", "", ""]

    # 捕获并忽略 SystemExit 异常
    Config("./test/test_config_file.yaml")

    # 比较生成的文件与目标文件
    assert filecmp.cmp(
        "./test/test_config_file.yaml", "src/AlistMediaRename/default.yaml"
    ), "生成的文件与目标文件不相同"

    # 删除生成的文件
    os.remove("./test/test_config_file.yaml")
