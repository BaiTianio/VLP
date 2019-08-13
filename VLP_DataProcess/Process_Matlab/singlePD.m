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

%%����ÿ��PD(1-32)�ڲ�ͬ�Ƕ��µ���Ӧ
% ���������ݼ���ȡ����ӦPD������(���ֵ)
PD_maxValue_cache=[];
x=[30:45,46:2:80];
for PD_num=1:32
    for times=1:3
        for angle=[30:45,46:2:80]
            PD_VarName=sprintf('PD%d_%d_%d',PD_num,angle,times);%PD��������������PD1_30_2(PD1��30��ʱ��2�βɼ�)
            eval([PD_VarName,sprintf('=data_%d_%d(:,%d);',angle,times,PD_num)]);%��ȡ��һ�βɼ�һ��angle��������PD����������
            PD_max=max(eval(PD_VarName));%Ѱ��PD�����е����ֵ
            PD_maxValue_cache=[PD_maxValue_cache,PD_max(1)];%���浱ǰPD_num,times,���нǶȵ�PD���ֵ
        end
        plot(x,PD_maxValue_cache);
        PD_maxValue_cache=[];%��ջ���
        hold on;
    end
    %��ͼ����
    legend('times=1','times=2','times=3');
    title(sprintf('PD%d',PD_num));
    savePath='./picture/SignlePD';
    if exist(savePath)==0   %���ļ��в����ڣ���ֱ�Ӵ���
        mkdir(savePath);
    end
    saveas(gcf,sprintf('./picture/SignlePD/PD%d.jpg',PD_num));%����ͼƬ
    hold off;
end

