# 在这个文件中编写代码
def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数：lst - 任意列表
    返回：bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 方法1: 使用集合来检查重复
    return len(lst) != len(set(lst))
    
    # 方法2: 使用字典统计频率（备选方案）
    # freq = {}
    # for item in lst:
    #     if item in freq:
    #         return True
    #     freq[item] = 1
    # return False


# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],    # 无重复
        [1, 2, 2],    # 有重复
        ["a", "b", "a"],    # 字符串重复
        [],    # 空列表
        [1, 1, 1, 1],    # 所有元素都重复
        [1, 2, 3, 4, 5],    # 无重复的长列表
        ["apple", "banana", "apple", "orange"]    # 字符串重复
    ]
    
    # 测试每个用例，编写具体测试代码
    print("重复元素检测测试结果：")
    print("=" * 40)
    
    for i, test_case in enumerate(test_cases, 1):
        result = has_duplicates(test_case)
        print(f"测试用例 {i}: {test_case}")
        print(f"结果: {result}")
        print(f"说明: {'有重复元素' if result else '无重复元素'}")
        print("-" * 30)
