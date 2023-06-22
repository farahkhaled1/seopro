@extends('layouts.user_type.auth')

@section('content')

  <div class="section min-vh-85 position-relative transform-scale-0 transform-scale-md-7">
    <div class="container">
      <div class="row pt-10">
        <div class="col-lg-1 col-md-1 pt-5 pt-lg-0 ms-lg-5 text-center">
          <a href="/user-profile" class="btn btn-white border-radius-lg p-2 mt-2" data-bs-toggle="tooltip" data-bs-placement="left" title="Home">
            <i class="fas fa-user p-2"></i>
          </a>
          <a href="/dashboard" class="btn btn-white border-radius-lg p-2 mt-2" data-bs-toggle="tooltip" data-bs-placement="left" title="Profile">
            <i class="fas fa-home p-2"></i>
          </a>
         
          
        </div>
        <div class="col-lg-8 col-md-11">
          <div class="d-flex">
            <div class="me-auto">
              {{-- <h1 class="display-1 font-weight-bold mt-n4 mb-0">28°C</h1> --}}
              <h1 class=" mb-0 ms-1">Welcome To Your Workspace {{ auth()->user()->name }}</h1>
            </div>
            

          </div>
          <div class="row mt-4">
            <div class="col-12 mt-4">
              <div class="card mb-4">
                <div class="card-header pb-0 p-3">
                  <h6 class="mb-1">Your Blogs</h6>
                  <p class="text-sm">Reach the right audience</p>
                </div>




                <div class="card-body p-3">
                  @php
                  $i = 1;
                  @endphp
                  <div class="row">
                      @foreach ($blogs as $blog)
                      <div class="col-xl-4 col-md-6 mb-xl-4 mb-4">
                          <div class="card card-blog card-plain">
                              <div class="position-relative">
                                  <a class="d-block shadow-xl border-radius-xl">
                                      <img src="../assets/img/home-decor-{{ $i % 3 + 1 }}.jpg" alt="img-blur-shadow" class="img-fluid shadow border-radius-xl">
                                  </a>
                              </div>
                              <div class="card-body px-1 pb-0">
                                  <p class="text-gradient text-dark mb-2 text-sm">Project #{{ $i }}</p>
                                  <a href="javascript:;">
                                      <h5>
                                          Blog {{ $i }}
                                      </h5>
                                  </a>
                                  <p class="mb-4 text-sm">
                                      {{ substr($blog->blog, 0, 50) }}...
                                  </p>
                                  <div class="d-flex align-items-center justify-content-between">
                                    <a href="{{ route('blog-editor',$blog->blogid) }}">
                                      <button type="button" class="btn btn-outline-primary btn-sm mb-0">Edit Blog</button>
                                    </a>
                                  </div>
                              </div>
                          </div>
                      </div>
                      @if ($i % 3 == 0)
                  </div>
                  <div class="row mt-4">
                      @endif
                      @php
                      $i++;
                      @endphp
                      @endforeach

                      <div class="col-xl-3 col-md-6 mb-xl-0 mb-4">
                        <div class="card h-100 card-plain border">
                            <div class="card-body d-flex flex-column justify-content-center text-center">
                                <a href="{{ route('editor') }}">
                                    <i class="fa fa-plus text-secondary mb-3"></i>
                                    <h5 class="text-secondary">New Blog</h5>
                                </a>
                            </div>
                        </div>
                    </div>
                  </div>
                 
                    
                  
              </div>
              



{{-- 
                <div class="card-body p-3">
                  <div class="row">
                    <div class="col-xl-3 col-md-6 mb-xl-0 mb-4">
                      <div class="card card-blog card-plain">
                        <div class="position-relative">
                          <a class="d-block shadow-xl border-radius-xl">
                            <img src="../assets/img/home-decor-1.jpg" alt="img-blur-shadow" class="img-fluid shadow border-radius-xl">
                          </a>
                        </div>
                        <div class="card-body px-1 pb-0">
                          <p class="text-gradient text-dark mb-2 text-sm">Project #1  </p>
                          <a href="javascript:;">
                            <h5>
                              Blog 1
                            </h5>
                          </a>
                          <p class="mb-4 text-sm">
                            Learn how to multiply your leadership and impact through this great example on...   </p>
                          <div class="d-flex align-items-center justify-content-between">
                            <button type="button" class="btn btn-outline-primary btn-sm mb-0">Edit Blog</button>
                            
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-3 col-md-6 mb-xl-0 mb-4">
                      <div class="card card-blog card-plain">
                        <div class="position-relative">
                          <a class="d-block shadow-xl border-radius-xl">
                            <img src="../assets/img/home-decor-2.jpg" alt="img-blur-shadow" class="img-fluid shadow border-radius-lg">
                          </a>
                        </div>
                        <div class="card-body px-1 pb-0">
                          <p class="text-gradient text-dark mb-2 text-sm">Project #2</p>
                          <a href="javascript:;">
                            <h5>
                              Blog 2
                            </h5>
                          </a>
                          {{-- <p class="mb-4 text-sm">
                            Music is something that every person has his or her own specific opinion about.
                          </p> 
                          <div class="d-flex align-items-center justify-content-between">
                            <button type="button" class="btn btn-outline-primary btn-sm mb-0">Edit Blog</button>
                            
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-3 col-md-6 mb-xl-0 mb-4">
                      <div class="card card-blog card-plain">
                        <div class="position-relative">
                          <a class="d-block shadow-xl border-radius-xl">
                            <img src="../assets/img/home-decor-3.jpg" alt="img-blur-shadow" class="img-fluid shadow border-radius-xl">
                          </a>
                        </div>
                        <div class="card-body px-1 pb-0">
                          <p class="text-gradient text-dark mb-2 text-sm">Project #3</p>
                          <a href="javascript:;">
                            <h5>
                              Blog 3
                            </h5>
                          </a>
                          {{-- <p class="mb-4 text-sm">
                            For example, a restauranteur could regularly blog about everything from their favorite farmers' markets, to amusing an...                      </p> 
                          <div class="d-flex align-items-center justify-content-between">
                            <button type="button" class="btn btn-outline-primary btn-sm mb-0">Edit Blog</button>
                          </div>
                        </div>
                      </div>
                    </div> --}}

                   
                  </div>
            
            
          </div>
        </div>
      </div>
    </div>
    
            </div>
          </div>
        </div>
      </div>
  </div>

@endsection
