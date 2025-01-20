'use client'
import React, { useEffect, useState } from 'react'
import { navLinks } from '../constants/constants'
import Link from 'next/link'

const Navbar = () => {
  const [navBg, setNavBg] = useState(false);

  useEffect(() => {
    const handler = () =>{
      if(window.scrollY>=90) setNavBg(true)
      if(window.scrollY < 90) setNavBg(false)
    };
  window.addEventListener('scroll', handler);
  return ()=> {
    window.removeEventListener('scroll', handler)
  }
  })

  return (
    <div className={` fixed ${navBg ? "bg-white shadow-md" : "fixed"} w-full transition-all duration-200 h-[12vh] z-[1000]`}>
      <div className='flex items-center h-full justify-between w-[90%] xl:w-[80%] mx-auto'>
        {/* { logo } */}
        <h1 className='text-xl md:tx-2xl font-extrabold'><span className='text-2xl md:text-4xl text-blue-500'>Uni</span>sek</h1>
        {/* { NavLinks } */}
        <div className='hidden lg:flex items-center space-x-10'>
          {navLinks.map((link) => {
            return (
              <Link href={link.url} key={link.id}>
                <p className='nav__link'>{link.label}</p>
              </Link>
            )
          })}
        </div>
        {/* { Button } */}
        <div className='flex items-center space-x-4'>
          <button className='md:px-8 md:py-2.5 px-6 py-2 text-white font-semibold text-base bg-blue-900 
          hover:bg-green-600 transition-all duration-200 rounded-full'>Join Us</button>
        </div>
      </div>
    </div>
  )
}

export default Navbar