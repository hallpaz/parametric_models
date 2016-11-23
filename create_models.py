import geom
import math
import numpy as np
from dataio import write_OFF

def tesselate_sphere(m, p, r=4, function=geom.sphere):
    vertex_buffer, index_buffer = [], []
    phi, theta = 0.00005, 0.00005
    theta_inc = (math.pi - 2*theta)/(p-1)
    phi_inc = 2*math.pi/m
    while theta < math.pi:
        while phi < 2*math.pi:
            vertex_buffer.append(function(phi, theta, r))
            phi = phi + phi_inc
        phi = 0.0
        vertex_buffer.append(function(phi, theta, r))
        theta = theta + theta_inc
    #compute triangulation
    for i in range(p):
        for j in range(m):
            if i+1 < p:
                index_buffer.append(np.array([i*(m+1) + j, (i+1)*(m+1) +j, i*(m+1) + j+1]))
                index_buffer.append(np.array([i*(m+1) + j+1, (i+1)*(m+1) + j, (i+1)*(m+1) + j+1]))
            #if i-1 > 0:
            #    index_buffer.append(np.array([(i-1)*(m+1) + j+1, i*(m+1) + j, i*(m+1) + j+1]))
    #std::cout << "indices vector size: " << indexBuffer.size() << std::endl;
    #write_OFF(vertexBuffer, indexBuffer, "/Users/hallpaz/malhaA.off");
    return vertex_buffer, index_buffer

def tesselate_cylinder(m, p, r = 2, h = 4, function = geom.cylinder):
    vertex_buffer, index_buffer = [], []
    theta, height = 0.0, -h/2
    theta_inc = 2*math.pi/m
    height_inc = h/p
    while height <= h:
        while theta < 2*math.pi:
            vertex_buffer.append(function(theta, height, r))
            theta = theta + theta_inc
        theta = 0.0
        vertex_buffer.append(function(theta, height, r))
        height = height + height_inc
    #compute triangulation
    for i in range(p):
        for j in range(m):
            if i+1 < p:
                index_buffer.append(np.array([(i+1)*(m+1) +j, i*(m+1) + j, i*(m+1) + j+1]))
                index_buffer.append(np.array([(i+1)*(m+1) + j, i*(m+1) + j+1, (i+1)*(m+1) + j+1]))
            #if i-1 > 0:
            #    index_buffer.append(np.array([(i-1)*(m+1) + j+1, i*(m+1) + j, i*(m+1) + j+1]))
    #std::cout << "indices vector size: " << indexBuffer.size() << std::endl;
    #write_OFF(vertexBuffer, indexBuffer, "/Users/hallpaz/malhaA.off");
    return vertex_buffer, index_buffer

def main():
    vertices, indices = tesselate_sphere(20, 10)
    write_OFF("models/sphere_lowpoly.off", vertices, indices)

    vertices, indices = tesselate_sphere(40, 20)
    write_OFF("models/sphere_midpoly.off", vertices, indices)

    vertices, indices = tesselate_sphere(80, 40)
    write_OFF("models/sphere_highpoly.off", vertices, indices)

    vertices, indices = tesselate_cylinder(20, 20)
    write_OFF("models/cylinder_lowpoly.off", vertices, indices)


if __name__ == '__main__':
    main()
