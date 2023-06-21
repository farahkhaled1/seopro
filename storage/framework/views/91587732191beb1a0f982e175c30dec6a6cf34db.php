<?php $__env->startSection('content'); ?>

<div class="row my-4">
  <div class="col-lg-8 col-md-6 mb-md-0 mb-4" style="margin-left:180px">
    <div class="card">
      <div class="card-header pb-0">


        
        <?php
        $analytics = \App\Models\Analytics::getDetails($domain_url);
    ?>
    

<h3>Track Your URL's Progress <span style="color: green"> </span></h3>

          <div class="row">


            <div class="col-lg-6 col-7">
              <h5 class="text-sm mb-0">
                <i class="fa fa-check text-info" aria-hidden="true"></i>
                <span class="font-weight-bold ms-1">A list of the URLs you have analyzed earlier:</span>
              </h5>
            </div>
            <div class="col-lg-6 col-5 my-auto text-end">
              <div class="dropdown float-lg-end pe-4">
                <a class="cursor-pointer" id="dropdownTable" data-bs-toggle="dropdown" aria-expanded="false">
                  <i class="fa fa-ellipsis-v text-secondary"></i>
                </a>
            
              </div>
            </div>
          </div>
        </div>
        <div class="card-body px-0 pb-2">
          <div class="table-responsive">
            <table class="table align-items-center mb-0">
              <thead>
              
                <tr>
                  <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7" title="">
                    Date
                  </th>
                  <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7" title="">
                    Domain
                  </th>
                  <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2" data-toggle="tooltip" title="">
                    <span>Domain Rank</span>
                    <i class="fa fa-question-circle ms-1 text-lowercase" data-toggle="tooltip"  title=""></i>
                  </th>
                  <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7" data-toggle="tooltip" title="">
                    <span  >Domain Authority</span>
                    <i class="fa fa-question-circle ms-1 text-lowercase" title=""></i>
                  </th>
                  <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7" data-toggle="tooltip" title="">
                    <span>CTR Scope</span>
                    <i class="fa fa-question-circle ms-1 text-lowercase"  title=""></i>
                  </th>  
                
                </tr>
                
              </thead>
              <tbody>
              

                
               <?php $__currentLoopData = \App\Models\Analytics::getDetails($domain_url); $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $analytics): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>

                 <?php
                   $domain_url = $analytics->domain_url;
                 ?>
              
                 <tr>
                  <td>
                    <div class="d-flex px-2 py-1">
                        <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm"><?php echo e($analytics->date); ?></h6>
                        </div>
                    </div>
                </td>
                     <td>
                         <div class="d-flex px-2 py-1">
                             <div class="d-flex flex-column justify-content-center">
                                 <h6 class="mb-0 text-sm"><?php echo e($analytics->domain_url); ?></h6>
                             </div>
                         </div>
                     </td>
                     <td>
                         <span class="text-xs font-weight-bold" style="color:red ; margin-left:50px "><?php echo e($analytics->domain_rank); ?></span>
                     </td>
                     <td class="align-middle text-center text-sm">
                         <span class="text-xs font-weight-bold"><?php echo e($analytics->domain_auth); ?></span>
                     </td>
                     <td class="align-middle">
                         <span class="text-xs font-weight-bold" style="margin-left: 100px"><?php echo e($analytics->ctr_scope); ?></span>
                     </td>
                 </tr>
             <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?> 
             

              </tbody>
            </table>
            
          </div>
          
        </div>
      
      </div>
      <br>
      <br>
      




<?php $__env->stopSection(); ?>
<?php $__env->startPush('dashboard'); ?>
  <script>
    window.onload = function() {
      var ctx = document.getElementById("chart-bars").getContext("2d");

      new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          datasets: [{
            label: "Sales",
            tension: 0.4,
            borderWidth: 0,
            borderRadius: 4,
            borderSkipped: false,
            backgroundColor: "#fff",
            data: [450, 200, 100, 220, 500, 100, 400, 230, 500],
            maxBarThickness: 6
          }, ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            }
          },
          interaction: {
            intersect: false,
            mode: 'index',
          },
          scales: {
            y: {
              grid: {
                drawBorder: false,
                display: false,
                drawOnChartArea: false,
                drawTicks: false,
              },
              ticks: {
                suggestedMin: 0,
                suggestedMax: 500,
                beginAtZero: true,
                padding: 15,
                font: {
                  size: 14,
                  family: "Open Sans",
                  style: 'normal',
                  lineHeight: 2
                },
                color: "#fff"
              },
            },
            x: {
              grid: {
                drawBorder: false,
                display: false,
                drawOnChartArea: false,
                drawTicks: false
              },
              ticks: {
                display: false
              },
            },
          },
        },
      });


      var ctx2 = document.getElementById("chart-line").getContext("2d");

      var gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);

      gradientStroke1.addColorStop(1, 'rgba(203,12,159,0.2)');
      gradientStroke1.addColorStop(0.2, 'rgba(72,72,176,0.0)');
      gradientStroke1.addColorStop(0, 'rgba(203,12,159,0)'); //purple colors

      var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

      gradientStroke2.addColorStop(1, 'rgba(20,23,39,0.2)');
      gradientStroke2.addColorStop(0.2, 'rgba(72,72,176,0.0)');
      gradientStroke2.addColorStop(0, 'rgba(20,23,39,0)'); //purple colors

      new Chart(ctx2, {
        type: "line",
        data: {
          labels: ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          datasets: [{
              label: "Mobile apps",
              tension: 0.4,
              borderWidth: 0,
              pointRadius: 0,
              borderColor: "#cb0c9f",
              borderWidth: 3,
              backgroundColor: gradientStroke1,
              fill: true,
              data: [50, 40, 300, 220, 500, 250, 400, 230, 500],
              maxBarThickness: 6

            },
       
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            }
          },
          interaction: {
            intersect: false,
            mode: 'index',
          },
          scales: {
            y: {
              grid: {
                drawBorder: false,
                display: true,
                drawOnChartArea: true,
                drawTicks: false,
                borderDash: [5, 5]
              },
              ticks: {
                display: true,
                padding: 10,
                color: '#b2b9bf',
                font: {
                  size: 11,
                  family: "Open Sans",
                  style: 'normal',
                  lineHeight: 2
                },
              }
            },
            x: {
              grid: {
                drawBorder: false,
                display: false,
                drawOnChartArea: false,
                drawTicks: false,
                borderDash: [5, 5]
              },
              ticks: {
                display: true,
                color: '#b2b9bf',
                padding: 20,
                font: {
                  size: 11,
                  family: "Open Sans",
                  style: 'normal',
                  lineHeight: 2
                },
              }
            },
          },
        },
      });
    }
  </script>
<?php $__env->stopPush(); ?>






                 
<?php echo $__env->make('layouts.user_type.auth', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH /Users/farahkhaled/Desktop/seopro-1/resources/views/analyticshistorydetails.blade.php ENDPATH**/ ?>