import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";
import MobileNav from "./components/Navbar/MobileNav";

// const geistSans = Geist({
//   variable: "--font-geist-sans",
//   subsets: ["latin"],
// });

// const geistMono = Geist_Mono({
//   variable: "--font-geist-mono",
//   subsets: ["latin"],
// });

const font = Poppins({
  weight:['100', '300', '400', '500', '700', '900', '200', '600', '800'],
  subsets: ['latin'],
});
export const metadata: Metadata = {
  title: "Unisek System",
  description: "A University selection app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${font.className} antialiased`}>
        <MobileNav />
        {children}
      </body>
    </html>
  );
}
