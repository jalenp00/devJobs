<template>
    <div class="form-control min-h-screen p-5">
        <h1 class="flex justify-center w-full sm:mt-14 2xl:mt-28 text-2xl">Create Job</h1>
        <div class="divider"></div>
        <!-- Input Rows -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-10">

            <!-- Right Row -->
            <div class="flex flex-col">
                <label class="input input-bordered flex items-center">
                    <input type="text" placeholder="Company"
                    v-model="job.company"/>
                </label>
                <label class="input input-bordered flex items-center mt-4">
                    <input type="text" placeholder="Title"
                    v-model="job.title" />
                </label>
                <label class="input input-bordered flex items-center mt-4">
                    <input type="text" placeholder="Location"
                    v-model="job.location" />
                </label>
                <label class="input input-bordered flex items-center mt-4">
                    <input type="number" placeholder="Years Needed" min="0" class="w-full"
                    v-model="job.yearsNeeded"  />
                </label>
            </div>

            <!-- Middle Row -->
        <div class="flex flex-col pl-10">
            <select class="select select-bordered w-full max-w-xs flex items-center"
            v-model="job.type">
                <option disabled selected value="null">Select One</option>
                <option value="remote">Remote</option>
                <option value="hybrid">Hybrid</option>
                <option value="Onsite">On-site</option>
            </select>
            <select class="select select-bordered w-full max-w-xs flex items-center mt-4"
            v-model="job.contract">
                <option disabled selected value="null">Select One</option>
                <option value="true">Contract</option>
                <option value="false">W-2</option>
            </select>
            <label class="input input-bordered flex items-center mt-4 w-[25vw]">
                <input type="text" placeholder="Technologies"
                v-model="currentTech" 
                @keydown.enter="addTech"/>
            </label>
            <div class="h-[3rem] w-full mt-4 rounded-lg">
                <div class="flex-1 justify-center h-full w-[25vw] items-center align-middle overflow-auto">
                    <div 
                    v-for="(tech, index) in job.techStack"
                    class="text-xs badge badge-secondary rounded-lg cursor-pointer"
                    style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-right: 5px;"
                    @click="removeTech(tech)"
                    >
                        {{ tech }}
                    </div>   
                </div>
            </div>
        </div>

        <!-- Left Row -->
        <div class="flex flex-col">
            <label class="input input-bordered flex items-center">
                <input type="number" placeholder="Days in office" min="0" class="w-full"
                v-model="job.daysInOffice" />
            </label>
            <label class="input input-bordered flex items-center mt-4">
                <input type="number" placeholder="$" min="0" class="w-full" 
                v-model="job.minSalary"/>
            </label>
            <div class="divider">To</div>
            <label class="input input-bordered flex items-center">
                <input type="number" placeholder="$$$" min="0" class="w-full" 
                v-model="job.maxSalary" />
            </label>
        </div>

        </div>

        <!-- Description Text Area -->
        <div class="h-[50vh]">
        <label class="label mt-10">
            <textarea class="textarea textarea-bordered w-full overscroll-none max-h-[40vh]" rows="6" placeholder="Job Description"
            v-model="job.description"
            ></textarea>
        </label>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-center">
            <button class="btn btn-secondary w-20" @click="">Save</button>
            <div class="divider mx-6"></div>
            <button class="btn btn-primary w-40" @click="createJob(job)">Submit</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import jobService from '~/service/jobService';
import { useRouter } from 'vue-router';

const job = ref<createJob>({
    title: '',
    company: '',
    location: '',
    type: null,
    contract: null,
    daysInOffice: null,
    minSalary: null,
    maxSalary: null,
    yearsNeeded: null,
    techStack: null,
    description: ''
});

const currentTech = ref('');
const router = useRouter();

const addTech = () => {
    if (currentTech.value.trim() !== '') {
        if (job.value.techStack) {
            job.value.techStack.push(currentTech.value.trim());
        } else {
            job.value.techStack = [currentTech.value.trim()];
        }
        currentTech.value = '';
    }
};

const removeTech = (tech: string) => {
    if (job.value.techStack) {
        job.value.techStack = job.value.techStack.filter(item => item !== tech);
    }
};

const createJob = async () => {
    if (job.value) {
        const response = await jobService.createJob(job.value);
        if (response.job) {
            router.push('/user/job');
        }
    }
}

</script>