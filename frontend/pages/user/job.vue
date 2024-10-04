<template>

  <FilterBar @filter="handleFilter"/>
  <!-- Job List -->
  <div v-if="errorMessage"> {{ errorMessage }}</div>
  <div v-else="filteredJobs" class="bg-base-100 mt-[8vh] sm:mt-[0vh] sm:pt-[12.75vh] sm:min-h-screen 2xl:pt-[10.5vh] xl:pb-10 p-2">
    <div class="w-[90vw] mt-4 ml-3 lg:mt-4 md:w-[75vw] lg:w-[25vw] sm:ml-[5vw] md:ml-[15vw] rounded-lg cursor-pointer" 
    v-for="(job, index) in filteredJobs"
    :class="{
        'card card-bordered border-accent': selectedJob && selectedJob.id === job.id,
        'card glass': !selectedJob || selectedJob && selectedJob.id !== job.id,
        'hidden lg:flex': selectedJob
      }"
    @click="selectJob(job)"
    >
      <div class="card-body job-text-color">
        <div class="flex justify-between items-center">
          <h2 class="card-title flex-grow text-left"> {{ job.title }}</h2>
          <span class="text-sm">{{ job.datePosted }}</span>
        </div>
        <h1>{{ job.company }} • {{ job.numApplicants }} applicants</h1>
        <p class="text-sm">
          {{ job.location  }} • {{ job.type }}
          <!--{{ job.remote ? 'Remote' : (job.hybrid ? `${job.location} • Hybrid` : job.location) }} -->
        </p>
        <p class="text-sm">${{ job.minSalary }} - ${{ job.maxSalary }} {{ job.contract ? '• Contract' :'' }}</p>
        <div class="inline-flex space-x-2">
          <div v-for="(tech, index) in job.techStack" :key="index" class="text-xs badge badge-secondary"
          style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            {{ tech }}
          </div>
        </div>
      </div>
    </div>
  </div>
  

  <!-- Single Job (large screens) -->
  <div v-if="selectedJob" class="hidden lg:flex fixed left-[45vw] top-[15vh] 2xl:top-[12vh] job-text-color" 
  >
    <div class="w-[30vw] h-[80vh] xxl:h-[90vh] border-2 border-secondary rounded-lg p-5 shadow-lg overflow-y-auto 2xl:overflow-hidden">
      <h2 class="text-xl font-semibold">{{ selectedJob.title }}</h2>
      <h3 class="text-lg">{{ selectedJob.company }}</h3>
      <div class="divider"></div>
      <p class="text-sm">{{ selectedJob.location }} • {{ selectedJob.type }}</p>
      <p class="text-sm">{{ selectedJob.contract ? 'Contract' : 'W-2' }}</p>
      <p class="text-sm">Salary: ${{ selectedJob.minSalary }} - ${{ selectedJob.maxSalary }}</p>
      <p class="text-sm">Years Needed: {{ selectedJob.yearsNeeded }}</p>
      <p class="text-sm">{{ selectedJob.numApplicants }} Applicants</p>
      <div class="divider"></div>
      <div class="flex flex-wrap">
        <div
          v-for="(tech, index) in selectedJob.techStack" 
          :key="index"
          class="text-xs badge badge-accent mr-1 mb-1"
        >
          {{ tech }}
        </div>
      </div>
      <div class="divider"></div>
      <h4 class="flex justify-center align-middle text-md font-semibold">Full Description:</h4>
      <p class="text-sm pt-5 xl:h-[60%]">{{ selectedJob.description }}</p>
      <div class="flex justify-center w-full pt-5">
        <button class="btn btn-primary mx-auto w-[60%] rounded-md">Apply</button>
      </div>
    </div>
  </div>

  <!-- Single Job (mobile only) -->
  <div v-if="selectedJob" class="lg:hidden w-full flex flex-col">
    <div class="pl-5 flex-grow overflow-auto">
      <h2 class="text-xl font-semibold">{{ selectedJob.title }}</h2>
      <h3 class="text-lg">{{ selectedJob.company }}</h3>
      <div class="divider"></div>
      <p class="text-sm">{{ selectedJob.location }}</p>
      <p class="text-sm">{{ selectedJob.type }}</p>
      <p class="text-sm">{{ selectedJob.contract ? 'Contract' : 'W-2' }}</p>
      <p class="text-sm">Salary: ${{ selectedJob.minSalary }} - ${{ selectedJob.maxSalary }}</p>
      <p class="text-sm">Years Needed: {{ selectedJob.yearsNeeded }}</p>
      <p class="text-sm" v-if="selectedJob.numApplicants">{{ selectedJob.numApplicants }} Applicants</p>
      <div class="divider"></div>
      <div class="flex flex-wrap">
        <div v-for="(tech, index) in selectedJob" :key="index" class="text-xs badge badge-accent mr-1 mb-1">
          {{ tech }}
        </div>
      </div>
      <div class="divider"></div>
      <h4 class="text-md font-semibold">Full Description:</h4>
      <p class="text-sm pt-5">{{ selectedJob.description }}</p>
    </div>
    <div class="absolute bottom-5 flex justify-between w-full bg-transparent pl-5">
      <button class="btn-ghost" @click="goBack()">←</button>
      <button class="btn btn-primary mx-auto w-[60%]">Apply</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import FilterBar from '@components/user/FilterBar.vue';
import jobService from '~/service/jobService';

interface Filter {
  location: string | null,
  type: string[] | null,
  contract: boolean,
  yearsNeeded: number | null,
  minSalary: number | null,
  maxSalary: number | null,
  techStack: string | null
}
const filter = ref<Filter>({
  location: null,
  type: null,
  contract: false,
  yearsNeeded: null,
  minSalary: 0,
  maxSalary: 0,
  techStack: null
});

const jobs = ref<ResponseJob[]>([]);
const isLoading = ref<boolean>(true);
const errorMessage = ref<string | null>(null);
const selectedJob = ref<Job | null>();
const scrollPosition = ref<number>(0);
const isMobile = ref<boolean>(false);

const props = defineProps<{
  searchTerm: string;
}>();

const getJobs = async () => {
  errorMessage.value = null; // Reset error
  try {
    const response = await jobService.getAllJobs();
    jobs.value = response.jobs;
  } catch (error) {
    errorMessage.value = 'Failed to load jobs. Please try again later.';
    console.error('Error fetching jobs:', error);
  }
};

const setMobile = () => {
  const width = window.innerWidth;
  isMobile.value = width <= 430;
};

onMounted(async () => {
  await getJobs();

  if (!isMobile.value) {
    selectedJob.value = jobs.value[0];
  };
})

onMounted( () => {
  
  setMobile();

  const mediaQueryList = window.matchMedia('(max-width: 430px)');
  
  const mediaQueryListener = () => setMobile();

  mediaQueryList.addEventListener('change', mediaQueryListener);

  onUnmounted(() => {
    mediaQueryList.removeEventListener('change', mediaQueryListener)
  })
});

const filteredJobs = computed(() => {
  if (jobs.value && (filter.value || searchTerm)) {
    return jobs.value.filter(job => {
      const searchMatch = props.searchTerm ? job.title.toLowerCase().includes(props.searchTerm.toLowerCase()) : true;
      const locationMatch = filter.value.location ? job.location.toLowerCase().includes(filter.value.location.toLowerCase()): true;
      const typeMatch = filter.value.type && filter.value.type.length > 0 
        ? filter.value.type.some(t => t === job.type)
        : true;
      const contractMatch = filter.value.contract ? !job.contract : true;
      const yearsNeededMatch = filter.value.yearsNeeded ? filter.value.yearsNeeded >= job.yearsNeeded : true;
      const minSalaryMatch = filter.value.minSalary ? filter.value.minSalary <= job.minSalary : true;
      const maxSalaryMatch = filter.value.maxSalary ? filter.value.maxSalary >= job.maxSalary : true;
      const techMatch = filter.value.techStack ? job.techStack.toLowerCase().match(filter.value.techStack.toLowerCase()) : true;
      return searchMatch && locationMatch && typeMatch && contractMatch && yearsNeededMatch && minSalaryMatch && maxSalaryMatch && techMatch;
    });
  } else {
    return jobs.value;
  }
});

const handleFilter = (newFilter : Filter) => {
  if (jobs.value) {
    filter.value = { ...newFilter };
  }
};

const selectJob = (job : Job) => {
  selectedJob.value = job;
  scrollPosition.value = window.scrollY;

  if (isMobile.value) {
    nextTick(() => {
      window.scrollTo(0,0);
    })
  }
};

const goBack = () => {
  selectedJob.value = null;
  nextTick(() => {
    window.scrollTo(0, scrollPosition.value);
  });
};
</script>

<style scoped>
</style>