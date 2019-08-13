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

%%绘制每个PD(1-32)在不同角度下的响应
% 从所有数据集中取出对应PD的数据(最大值)
PD_maxValue_cache=[];
x=[30:45,46:2:80];
for PD_num=1:32
    for times=1:3
        for angle=[30:45,46:2:80]
            PD_VarName=sprintf('PD%d_%d_%d',PD_num,angle,times);%PD变量命名，例：PD1_30_2(PD1在30°时第2次采集)
            eval([PD_VarName,sprintf('=data_%d_%d(:,%d);',angle,times,PD_num)]);%提取（一次采集一个angle）数据中PD的所有数据
            PD_max=max(eval(PD_VarName));%寻找PD数据中的最大值
            PD_maxValue_cache=[PD_maxValue_cache,PD_max(1)];%保存当前PD_num,times,所有角度的PD最大值
        end
        plot(x,PD_maxValue_cache);
        PD_maxValue_cache=[];%清空缓存
        hold on;
    end
    %绘图部分
    legend('times=1','times=2','times=3');
    title(sprintf('PD%d',PD_num));
    savePath='./picture/SignlePD';
    if exist(savePath)==0   %该文件夹不存在，则直接创建
        mkdir(savePath);
    end
    saveas(gcf,sprintf('./picture/SignlePD/PD%d.jpg',PD_num));%保存图片
    hold off;
end

