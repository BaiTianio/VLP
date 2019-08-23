%����汾��ȷ��angle��times��һ�����ݣ�Ȼ��ֱ�ȡÿ��PD����Ӧ�����ֵ��

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
x=1:8;
for PDarray=1:4  %����PD
    for angle=[30:45,46:2:80]
        for times=1:3
            PD_num=PDarray:4:32;%�ֱ�ȡ����PD
            eval(sprintf('temp=data_%d_%d(:,PD_num);',angle,times));%��ȡ����
            y=max(temp);%Ѱ���������ֵ
            plot(x,y);
            hold on;
        end
        title(sprintf('PDarray=%d  angle=%d',PDarray,angle));
        legend('times=1','times=2','times=3');
        savePath='./picture/8PDsV2';
        if exist(savePath)==0   %���ļ��в����ڣ���ֱ�Ӵ���
            mkdir(savePath);
        end
        saveas(gcf,sprintf('./picture/8PDsV2/PDarray%d_%d.jpg',PDarray,angle)); %ͼƬ�洢����ʽ��PDarray1_30(��һ��PD��30��)
        hold off
    end
end

    
   


