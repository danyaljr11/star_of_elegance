import{b as l,u as v,j as s}from"./index-CkvAdKOf.js";import{d as j}from"./deleteicon-4Sc3Kd4X.js";import{S as w}from"./SideBar-Cb9YIg1_.js";/* empty css                  */import{a as m}from"./axios-upsvKRUO.js";import{A as N}from"./api-oWY9WQi5.js";import"./index-Bi3ZVyb4.js";import"./iconBase-CQ5bDd8R.js";const D="data:image/svg+xml,%3csvg%20width='35'%20height='35'%20viewBox='0%200%2035%2035'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M4.375%2030.625V24.4271L23.625%205.21354C23.9167%204.94618%2024.239%204.73958%2024.5919%204.59375C24.9448%204.44792%2025.3152%204.375%2025.7031%204.375C26.091%204.375%2026.4678%204.44792%2026.8333%204.59375C27.1989%204.73958%2027.5149%204.95833%2027.7812%205.25L29.7865%207.29167C30.0781%207.55903%2030.291%207.875%2030.4252%208.23958C30.5594%208.60417%2030.626%208.96875%2030.625%209.33333C30.625%209.72222%2030.5584%2010.0931%2030.4252%2010.446C30.292%2010.799%2030.0791%2011.1208%2029.7865%2011.4115L10.5729%2030.625H4.375ZM25.6667%2011.375L27.7083%209.33333L25.6667%207.29167L23.625%209.33333L25.6667%2011.375Z'%20fill='%23667085'/%3e%3c/svg%3e";function I(){const[i,x]=l.useState([]),[a,n]=l.useState(1),r=2,o=v();l.useEffect(()=>{(async()=>{try{const t=await m.get(N.GET.SERVICELIST);x(t.data.reverse())}catch{o("/error")}})()},[i]);const c=Math.ceil(i.length/r),d=a*r,p=d-r,g=i.slice(p,d),h=()=>n(e=>e<c?e+1:e),f=()=>n(e=>e>1?e-1:e),u=async e=>{try{const t=await m.delete(`https://starofelegance.com/api/services/${e}/delete/`)}catch{}},b=(e,t)=>{window.confirm(`Are you sure you want to delete this service ${t} ?`)&&(u(e),alert(`this service:${t} has been deleted`),fetchData())};return s.jsxs("div",{className:"md:flex gap-14",children:[s.jsx(w,{}),s.jsxs("div",{className:"pl-14 md:pl-0",children:[s.jsx("p",{className:"mb-10 text-black font-bold text-2xl mt-32 Poppins",children:"Dashboard"}),s.jsx("p",{className:"font-semibold text-2xl mb-14 Poppins",children:"Services"}),g.map((e,t)=>s.jsxs("div",{className:"flex flex-col md:flex-row gap-10 md:w-[1100px] justify-center items-center mb-20 container-services2",children:[s.jsxs("div",{className:"flex bg-[#D9D9D9] rounded-lg child-services",children:[s.jsx("img",{className:"w-[350px] h-[320px]",src:e.picture,alt:e.name}),s.jsxs("div",{className:"pl-8",children:[s.jsx("p",{className:"font-normal text-3xl text-black kanit mb-12",children:e.name}),s.jsx("p",{className:"font-normal text-xl text-black nun mb-14",children:e.description})]})]}),s.jsx("div",{onClick:()=>b(e.id,e.name),className:" hover:cursor-pointer bg-[#D9D9D9] flex justify-center items-center w-44 gap-3.5  h-14 rounded-lg",children:s.jsx("img",{src:j,className:"w-8",alt:"icon"})}),s.jsx("div",{onClick:()=>o("/dashboard/service/edit/"+e.id),className:" hover:cursor-pointer bg-[#D9D9D9] flex justify-center items-center w-44 gap-3.5  h-14 rounded-lg",children:s.jsx("img",{src:D,className:"w-8",alt:"icon"})})]},t)),s.jsxs("div",{className:"flex justify-center mt-8 gap-4",children:[s.jsx("button",{onClick:f,disabled:a===1,className:`px-4 py-2 rounded-lg ${a===1?"bg-gray-300 cursor-not-allowed":"bg-blue-500 text-white hover:bg-blue-700"}`,children:"Previous"}),s.jsxs("span",{className:"text-lg font-semibold",children:[a," / ",c]}),s.jsx("button",{onClick:h,disabled:a===c,className:`px-4 py-2 rounded-lg ${a===c?"bg-gray-300 cursor-not-allowed":"bg-blue-500 text-white hover:bg-blue-700"}`,children:"Next"})]})]})]})}export{I as default};
