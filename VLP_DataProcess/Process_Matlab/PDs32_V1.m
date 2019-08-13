clc;clear all;
%%���ݶ�ȡ,��ȡ�ļ����е��������ݡ�
%������������data_angle_times
file_list=dir('.\data_csv\*.csv');
for n=1:length(file_list)
    path=['.\data_csv\',file_list(n).name];
    data_cache=csvread(path);%���ݶ�ȡ����
    data_name=file_list(n).name(1:end-4);%������������Ӧ�ļ�����
    eval([data_name,'=data_cache;']);%�����ݻ��渳����Ӧ�ļ����ı���
end

%%��ͼ
x=1:32;
PD_num=1:32;
for angle=[30:45,46:2:80]
    for times=1:3
        eval(sprintf('temp=data_%d_%d;',angle,times));%��ȡ����
        [max_rows,max_cols]=find(temp==max(max(temp)));%Ѱ�����������
        y=temp(max_rows(1),PD_num);
        plot(x,y);
        hold on;
    end
    title(sprintf('angle=%d',angle));
    legend('times=1','times=2','times=3');
    savePath='./picture/32PDsV1';
    if exist(savePath)==0   %���ļ��в����ڣ���ֱ�Ӵ���
        mkdir(savePath);
    end
    saveas(gcf,sprintf('./picture/32PDsV1/Angle_%d.jpg',angle)); %ͼƬ�洢����ʽ��PDarray1_30(��һ��PD��30��)
    hold off
end

