nalu_abl_mesh:
  output_db: ellipticWingMesh.exo

  spec_type: bounding_box

  vertices:
    - [-10.0, -15.0, -15.0]
    - [20.0, 15.0, 15.0]

  mesh_dimensions: [240, 240, 240]

  xmin_boundary_name: inflow
  xmax_boundary_name: outflow
  ymin_boundary_name: left
  ymax_boundary_name: right
  zmin_boundary_name: bottom
  zmax_boundary_name: top

