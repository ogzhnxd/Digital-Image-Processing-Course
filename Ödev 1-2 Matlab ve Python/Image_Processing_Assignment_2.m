a = imread("cameraman.tif");

b = imread("text.tif");

m = uint8(double(a) + 255*double(b));

% For seperation of cameraman

k = m;

for idx = find(m == 255)
    k(idx) = a(idx);
end

% For seperation of text
text = not((m > 250));
% Showing images
subplot(2, 3, 1)
title("cameraman")
imshow(a)

subplot(2, 3, 2)
title("text")
imshow(b)

subplot(2, 3, 3)
title("merged image")
imshow(m)

subplot(2, 3, 4)
title("separated cameraman")
imshow(k)

subplot(2, 3, 5)
title("seperated text")
imshow(text)


