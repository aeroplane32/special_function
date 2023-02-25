figure(1);
drawarrow([0,0],[1/sqrt(2),1/sqrt(2)]);
drawarrow([1/sqrt(2),1/sqrt(2)],[1,0]);
circ(0,0,1);
circ(1/sqrt(2),1/sqrt(2),1);
axis equal;

function y=circ(x,y,r)
    para=[x-r y-r 2*r 2*r];
    rectangle('position', para, 'curvature', [1 1]);
    y=0;
end

function drawarrow(x,y,lineType,ax)
    switch nargin
        case 2
            lineType='arrow';
            ax=gca;
        case 3
            ax=gca;
    end
    % 调整坐标大小以适应箭头长度
    xlim=ax.XLim;
    ylim=ax.YLim;
    xlimmin=xlim(1);xlimmax=xlim(2);
    ylimmin=ylim(1);ylimmax=ylim(2);
    if xlimmin>min(x(1),y(1)), xlimmin=min(x(1),y(1));end
    if xlimmax<max(x(1),y(1)), xlimmax=max(x(1),y(1));end
    if ylimmin>min(x(2),y(2)), ylimmin=min(x(2),y(2));end
    if ylimmax<max(x(2),y(2)), ylimmax=max(x(2),y(2));end
    ax.XLim = [xlimmin,xlimmax];
    ax.YLim = [ylimmin,ylimmax];
    xlim=ax.XLim;
    ylim=ax.YLim;
    pos=ax.Position;
    x_ratio = pos(3)/(xlim(2)-xlim(1));
    y_ratio = pos(4)/(ylim(2)-ylim(1)); % 缩放比例
    orig_pos=[-xlim(1)*x_ratio+pos(1),-ylim(1)*y_ratio+pos(2)]; % figure坐标系中的原点坐标
    x=x.*[x_ratio,y_ratio];y=y.*[x_ratio,y_ratio];
    x=x+orig_pos;y=y+orig_pos;
    annotation(lineType,[x(1),y(1)],[x(2),y(2)])
end
