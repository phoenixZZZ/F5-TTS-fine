import json
import csv
import os

def json_to_csv(json_file_path, csv_file_path):
    # 打开输出 CSV 文件
    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')  # 使用 | 作为分隔符
        
        # 如果 JSON 文件是逐行写入的 JSONL 格式
        if json_file_path.endswith('.jsonl'):
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                for line in json_file:
                    # 解析每一行的 JSON 对象
                    data = json.loads(line.strip())
                    # 提取 wav 文件名（去掉路径）和 text 字段
                    wav_path = data.get('wav', '')
                    wav_filename = os.path.basename(wav_path)  # 提取文件名
                    text = data.get('text', '')
                    # 写入 CSV
                    writer.writerow([wav_filename, text])
        
        # 如果 JSON 文件是一个包含列表的单文件
        else:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                data_list = json.load(json_file)  # 假设是列表
                for data in data_list:
                    # 提取 wav 文件名（去掉路径）和 text 字段
                    wav_path = data.get('wav', '')
                    wav_filename = os.path.basename(wav_path)  # 提取文件名
                    text = data.get('text', '')
                    # 写入 CSV
                    writer.writerow([wav_filename, text])

    print(f"转换完成！CSV 文件已保存到：{csv_file_path}")

# 示例用法
if __name__ == "__main__":
    # 输入和输出文件路径
    json_input = "/home/huangjunren/F5-TTS/org_data/Emilia_dataset/ZH/ZH_B00041.jsonl"  # 替换为你的 JSON 文件路径
    csv_output = "/home/huangjunren/F5-TTS/org_data/Emilia_dataset/ZH/metadata.csv"  # 替换为目标 CSV 文件路径
    
    # 执行转换
    json_to_csv(json_input, csv_output)