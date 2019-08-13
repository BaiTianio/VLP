clc;clear all;
%%数据读取,读取文件夹中的所有数据。
%数据命名规则：data_angle_times
file_list=dir('.\data_csv\*.csv');
for n=1:length(file_list)
    path=['.\data_csv\',file_list(n).name];
    data_cache=csvread(path);%数据读取缓存
    data_name=file_list(n).name(1:end-4);%变量命名（对应文件名）
    eval([data_name,'=data_cache;']);%将数据缓存赋给对应文件名的变量
end

%%绘图
x=1:32;
PD_num=1:32;
for angle=[30:45,46:2:80]
    for times=1:3
        eval(sprintf('temp=data_%d_%d;',angle,times));%提取数据
        [max_rows,max_cols]=find(temp==max(max(temp)));%寻找数据最大行
        y=temp(max_rows(1),PD_num);
        plot(x,y);
        hold on;
    end
    title(sprintf('angle=%d',angle));
    legend('times=1','times=2','times=3');
    savePath='./picture/32PDsV1';
    if exist(savePath)==0   %该文件夹不存在，则直接创建
        mkdir(savePath);
    end
    saveas(gcf,sprintf('./picture/32PDsV1/Angle_%d.jpg',angle)); %图片存储名格式：PDarray1_30(第一组PD在30度)
    hold off
end

