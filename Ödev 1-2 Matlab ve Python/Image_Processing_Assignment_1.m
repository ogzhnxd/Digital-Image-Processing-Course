
% Creating background
img = zeros(256,256);
img1 = zeros(256,256);
img = uint8(img);
img1 = uint8(img1);

% Drawing \ part od X
for i = 64:192
    for j = 64:192
        if i == j
            img(i-10:i+10,j-10:j+10) = 5;
        end    
    end    
end

% / part of X
mirror_img = flip(img, 2);
% Merge \ and /
img = img | mirror_img;

% Drawing cross
img1(118:138,32:224) = 2; 
img1(32:224, 118:138) = 2;

% Adding + and X side by side
img3 = cat(2,img,img1);

% Changing X grayscale value to 5
img3(img3 == 1) = 5;

% Making visible X
cross = img3;
cross(cross > 4) = 255;

% Making visible +
plus = cross; % Making threshold on X !
plus = (plus > 1 & plus <= 3);

% Show results
subplot(2, 3, 1)
imshow(img3)

subplot(2, 3, 2)
imshow(cross)

subplot(2, 3, 3)
imshow(plus)

subplot(2, 3, 4)
imhist(img3)

subplot(2, 3, 5)
imhist(cross);

subplot(2, 3, 6)
imhist(plus);
