from minio import Minio
# from minio.error import ResponseError
import csv

# Minio服务器的访问信息
endpoint_url = "airlab-share-01.andrew.cmu.edu:9000"
# access_key = "your-access-key"
# secret_key = "your-secret-key"

# 初始化Minio客户端
client = Minio(endpoint_url, secure=False)

# 要列出文件的桶名称
audio_bucket_name = "tartanaviation-audio"
vision_bucket_name = "tartanaviation-vision"
adsb_bucket_name = "tartanaviation-adsb"

audio_list = []
vision_list = []
adsb_list = []



audio_objects = client.list_objects(audio_bucket_name, recursive=True)

for obj in audio_objects:
    fname = obj.object_name
    # print(fname)
    date = fname.split('/')[1]+"-"+fname.split('/')[3][:5]
    # print(fname, date)
    if 'kagc' in fname:
        audio_list.append(date)

# vision_objects = client.list_objects(vision_bucket_name, recursive=True)
# for obj in vision_objects:
#     print(obj.object_name)
with open('./vision/weather_stats.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    video_folders = []
    for row in reader:
        video_name, aircraft, visibility, mist, fog, haze, sky_cover_l1, cloud_height_l1, rain, snow = row
        
        date = video_name[2:12]
        print(video_name, date)
        vision_list.append(date)

print(sorted(set(vision_list)))
print("\n")
print(sorted(set(audio_list)))

# print(sorted(list(set(vision_list).intersection(set(audio_list)))))
adsb_objects = client.list_objects(adsb_bucket_name, recursive=True)
for obj in adsb_objects:
    print(obj.object_name)


# try:
#     # 列出指定桶中的所有对象
    
# except: #ResponseError as err:
#     # print(f"Error: {err}")
#     pass

# buckets = client.list_buckets()

# for bucket in buckets:
#     print(bucket.name)


'''
['2022-06-24', '2022-06-25', '2022-06-26', '2022-06-27', '2022-06-28', 
'2022-06-29', '2022-06-30', '2022-07-01', '2022-07-19', '2022-07-20', 
'2022-07-21', '2022-07-24', '2022-07-25', '2022-08-23', '2022-08-24', 
'2022-08-25', '2022-08-26', '2022-08-31', '2022-09-02', '2022-09-03', 
'2022-09-04', '2022-09-05', '2022-09-07', '2022-09-08', '2022-09-09', 
'2022-09-10', '2022-09-11', '2022-11-17', '2022-11-18', '2022-11-19', 
'2022-11-20', '2022-11-21', '2022-11-22', '2022-11-23', '2022-11-24', 
'2022-11-25', '2022-11-26', '2022-11-27', '2022-11-28', '2022-11-29', 
'2022-12-15', '2022-12-16', '2022-12-18', '2022-12-19', '2022-12-20', 
'2022-12-21', '2022-12-27', '2022-12-28', '2022-12-29', '2022-12-30', '2023-02-17']
'''
