import numpy as np
import pandas as pd

def test_numpy():
    # 创建一个一维数组
    array_1d = np.array([1, 2, 3, 4, 5])
    print("一维数组:", array_1d)

    # 创建一个二维数组
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("二维数组:\n", array_2d)

    # 数组的形状
    print("一维数组的形状:", array_1d.shape)
    print("二维数组的形状:", array_2d.shape)

    # 数组的维度
    print("一维数组的维度:", array_1d.ndim)
    print("二维数组的维度:", array_2d.ndim)

    # 数组的类型
    print("一维数组的类型:", array_1d.dtype)
    print("二维数组的类型:", array_2d.dtype)

    # 数组的数学运算
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])

    print("数组相加:", array_a + array_b)
    print("数组相减:", array_a - array_b)
    print("数组相乘:", array_a * array_b)
    print("数组相除:", array_a / array_b)

    # 使用 numpy 的内置函数
    print("数组的和:", np.sum(array_a))
    print("数组的平均值:", np.mean(array_a))
    print("数组的标准差:", np.std(array_a))
    print("数组的最大值:", np.max(array_a))
    print("数组的最小值:", np.min(array_a))

    # 矩阵乘法
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    print("矩阵乘法:\n", np.dot(matrix_a, matrix_b))

    # 生成随机数
    random_array = np.random.rand(3, 3)
    print("随机数组:\n", random_array)


def test_pandas():
    # 创建一个简单的 DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)
    print("原始 DataFrame:\n", df)

    # 查看 DataFrame 的基本信息
    print("\nDataFrame 的基本信息:")
    print(df.info())

    # 查看 DataFrame 的统计信息
    print("\nDataFrame 的统计信息:")
    print(df.describe())

    # 选择某一列
    print("\n选择 'Name' 列:")
    print(df['Name'])

    # 选择多列
    print("\n选择 'Name' 和 'Age' 列:")
    print(df[['Name', 'Age']])

    # 按条件筛选数据
    print("\n筛选年龄大于 25 的行:")
    print(df[df['Age'] > 25])

    # 添加新列
    df['Salary'] = [70000, 80000, 75000, 90000]
    print("\n添加 'Salary' 列后的 DataFrame:")
    print(df)

    # 修改某一列的值
    df['Age'] = df['Age'] + 1
    print("\n修改 'Age' 列后的 DataFrame:")
    print(df)

    # 删除某一列
    df = df.drop(columns=['City'])
    print("\n删除 'City' 列后的 DataFrame:")
    print(df)

    # 按某一列排序
    df_sorted = df.sort_values(by='Age', ascending=False)
    print("\n按 'Age' 列降序排序后的 DataFrame:")
    print(df_sorted)

    # 保存 DataFrame 到 CSV 文件
    df.to_csv('output.csv', index=False)
    print("\nDataFrame 已保存到 'output.csv'")

    # 从 CSV 文件读取 DataFrame
    df_from_csv = pd.read_csv('output.csv')
    print("\n从 'output.csv' 读取的 DataFrame:")
    print(df_from_csv)


if __name__ == "__main__":
    test_numpy()
    test_pandas()