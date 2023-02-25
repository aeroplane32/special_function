A=2; T=8; tau=4; w=2*pi/T;
x=linspace(-5,5,500);
y=A*(heaviside(x+2)-heaviside(x-2));
figure(1);
subplot(221);
plot(linspace(-4,4,500),y,'linewidth',1); grid on; xlim([-5,5]); ylim([-0.5,2.5]); 
xlabel('$t$','interpreter', 'latex'); ylabel('$f(t)$','interpreter', 'latex');
y=fc(x,3);
subplot(222);
plot(x,y,'linewidth',1); axis tight; grid on; ylim([-0.5,2.5]); 
xlabel('$t$','interpreter', 'latex'); ylabel('$S_3[f](t)$', 'interpreter', 'latex'); title('n=3');
y=fc(x,15);
subplot(223);
plot(x,y,'linewidth',1); axis tight; grid on; ylim([-0.5,2.5]); 
xlabel('$t$','interpreter', 'latex'); ylabel('$S_{15}[f](t)$', 'interpreter', 'latex'); title('n=15');
subplot(224);
y=fc(x,70);
plot(x,y,'linewidth',1); axis tight; grid on; ylim([-0.5,2.5]); 
xlabel('$t$','interpreter', 'latex'); ylabel('$S_{70}[f](t)$', 'interpreter', 'latex'); title('n=70');



function y=fc(x,n)
    y=zeros(1,500);
    for m=-n:n
        y=y+sinc(m/2)*exp(1i*m*pi/4*x);
    end
end