console.log("I'm working!");
const title = document.getElementsByTagName('h1')[0];
console.log(title);
title.addEventListener('mouseover', () =>
{
    title.style.color = 'green';
});

title.addEventListener('mouseout', () =>
{
    title.style.color = 'white';
});

const subTitleOne = document.getElementsByTagName('h2')[0];
console.log(subTitleOne);

subTitleOne.addEventListener('mouseover', () =>
{
    subTitleOne.style.fontSize = 'larger';
});

subTitleOne.addEventListener('mouseout', () =>
{
    subTitleOne.style.fontSize = 'medium';
});
