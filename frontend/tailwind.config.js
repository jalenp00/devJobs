/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  daisyui: {
    themes: [ 
      {
        synthwave: {
          ...require("daisyui/src/theming/themes")["synthwave"],
          ".job-text-color": {
            "color": "rgb(214 211 209)"
          }
        },
        lofi :{
          ...require("daisyui/src/theming/themes")["lofi"],
          ".job-text-color": {
            "color": "black"
          },
          background: "#ffffff"
        }
      },
      "winter", "halloween", "business"
    ]
  },
  plugins: [
    require('daisyui'),
  ],
}

