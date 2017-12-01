Simulations:
  - name: sim1
    time_integrator: ti_1
    optimizer: opt1

linear_solvers:

  - name: solve_scalar
    type: tpetra
    method: gmres
    preconditioner: sgs 
    tolerance: 1e-5
    max_iterations: 50
    kspace: 50
    output_level: 0

  - name: solve_cont
    type: tpetra
    method: gmres 
    preconditioner: muelu 
    tolerance: 1e-5
    max_iterations: 50
    kspace: 50
    output_level: 0
    muelu_xml_file_name: ../../common/milestone.xml
    summarize_muelu_timer: no

realms:

  - name: realm_1
    mesh: ellipticWingMesh.exo
    use_edges: no 
    automatic_decomposition_type: rcb

    equation_systems:
      name: theEqSys
      max_iterations: 2 
  
      solver_system_specification:
        velocity: solve_scalar
        pressure: solve_cont
   
      systems:

        - LowMachEOM:
            name: myLowMach
            max_iterations: 1
            convergence_tolerance: 1e-5

    initial_conditions:

      - constant: ic_1
        target_name: fluid_part
        value:
          pressure: 0.0
          velocity: [10.0,0.0,0.0]

    material_properties:
      target_name: fluid_part
      specifications:
        - name: density
          type: constant
          value: 1.225

        - name: viscosity
          type: constant
          value: 1.846e-5

    boundary_conditions:

    - inflow_boundary_condition: bc_1
      target_name: inflow
      inflow_user_data:
        velocity: [10.0,0.0,0.0]

    - open_boundary_condition: bc_2
      target_name: outflow
      open_user_data:
        pressure: 0.0
        velocity: [10.0,0.0,0.0]

    - symmetry_boundary_condition: bc_3
      target_name: left
      symmetry_user_data:

    - symmetry_boundary_condition: bc_4
      target_name: right
      symmetry_user_data:

    - symmetry_boundary_condition: bc_5
      target_name: bottom
      symmetry_user_data:

    - symmetry_boundary_condition: bc_6
      target_name: top
      symmetry_user_data:

    solution_options:
      name: myOptions
      use_consolidated_solver_algorithm: yes

      options:

        - hybrid_factor:
            velocity: 0.0

        - limiter:
            pressure: no
            velocity: no

        - projected_nodal_gradient:
            pressure: element
            velocity: element 

        - element_source_terms:
            momentum: [momentum_time_derivative, advection_diffusion, actuator]
            continuity: [advection]

    actuator:
      type: ActLineFAST
      search_method: boost_rtree
      search_target_part: fluid_part

      n_turbines_glob: 1
      simStart: init
      dry_run:  False
      debug:    True
      t_start: 0.0
      t_max:    30.0
      dt_fast: 0.005
      n_every_checkpoint: 250

      Turbine0:
        num_force_pts_blade: 50
        num_force_pts_tower: 0
        epsilon: [ 1.0, 1.0, 1.0 ]
        turbine_base_pos: [ 5.0, 6.5, -90.0 ]
        turbine_hub_pos: [ 5.0, 6.5, 0.0 ]
        restart_filename: "blah"
        fast_input_filename: "EllipticWing.fst"
        turb_id:  1
        turbine_name: elliptic_wing

    output:
      output_data_base_name: out/ellipticWing.e
      output_frequency: 250
      output_node_set: no
      output_variables:
       - velocity
       - pressure
       - actuator_source

    restart:
      restart_data_base_name: rst/ellipticWing.rst
      restart_frequency: 250
      restart_start: 1
      compression_level: 9
      compression_shuffle: yes  

Time_Integrators:
  - StandardTimeIntegrator:
      name: ti_1
      start_time: 0
      termination_step_count: 6000
      time_step: 0.005
      time_stepping_type: fixed
      time_step_count: 0
      second_order_accuracy: yes

      realms:
        - realm_1
