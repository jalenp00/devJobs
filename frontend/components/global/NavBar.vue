<template>
    <div class="navbar fixed top-0 z-50 bg-base-100 h-[5vh]">
        <div class="flex justify-center align-middle">
            <a class="btn btn-primary btn-ghost sm:text-large md:text-xl lg:text-xl">devJobs</a>
        </div>
        <div class="flex-grow justify-center align-middle relative">
            <label class="input input-bordered flex items-center gap-2 sm:w-[30vw] md:w-[35vw] lg:w-[25vw]">
                <input type="text" class="grow" placeholder="Search" />
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor"
                    class="h-4 w-4 opacity-70">
                    <path fill-rule="evenodd"
                        d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
                        clip-rule="evenodd" />
                </svg>
            </label>
        </div>
        <div class="flex">
            <div class="sm:pl-10 md:pr-5 lg:pr-10 "><button class="btn btn-primary w-15">My Jobs</button></div>
            <div class="dropdown dropdown-end sm:pr-1 md:pr-5 lg:pr-5">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <img alt="Tailwind CSS Navbar component"
                            src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                    </div>
                </div>
                <ul tabindex="0"
                    class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li>
                        <a class="justify-between">
                            Profile
                            <span class="badge">New</span>
                        </a>
                    </li>
                    <li><a>Settings</a></li>
                    <li><a>Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
</template>